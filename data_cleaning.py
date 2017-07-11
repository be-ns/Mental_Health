import pandas as pd
import numpy as np


def _gender_category(data):
    male = ['male', 'm', 'mal','make', 'man', 'guy', 'mail', 'male-ish', 'maile', 'male (cis)', 'cis male']
    female = ['female', 'femake', 'femail', 'cis-female\femme', 'female ', 'woman', 'girl']
    data.Gender = data.Gender.apply(lambda x: 1 if x.lower() in male else 2 if x.lower() in female else 3)
    return data


def _drop_(data):
    data.drop(labels=['coworkers', 'comments', 'Timestamp', 'state', 'self_employed', 'benefits', ], axis = 1, inplace = True)
    return data


def _tech(data):
    data.tech_company = data.tech_company.apply(lambda x: 1 if x == 'Yes' else 0)
    return data


def _check_for_socialized_healthcare(data):
    socialized = {'United States': 68.35, 'Canada':69.77, 'United Kingdom': 74.26, \
    'Bulgaria': 52.72, 'France': 78.40, 'Portugal': 69.73, \
    'Netherlands': 82.22, 'Switzerland': 71.74, 'Poland': 62.33, \
    'Australia': 75.42, 'Germany': 75.99, 'Russia': 56.13, \
    'Mexico': 69.82, 'Brazil': 52.44, 'Slovenia': 65.15, \
    'Costa Rica': 0.0, 'Austria': 79.47, 'Ireland': 53.12, \
    'India': 67.50, 'South Africa': 62.55, 'Italy': 66.69, \
    'Sweden': 70.56, 'Colombia': 66.79, 'Latvia': 0.0, \
    'Romania': 53.84, 'Belgium': 79.85, 'New Zealand': 71.65, \
    'Zimbabwe': 0.0, 'Spain': 76.34, 'Finland': 74.61, \
    'Uruguay': 0.0, 'Israel': 74.98, 'Bosnia and Herzegovina': 60.57, \
    'Hungary': 52.29, 'Singapore': 68.50, 'Japan': 81.33, \
    'Nigeria': 0.0, 'Croatia': 65.05, 'Norway': 74.96, \
    'Thailand': 80.57, 'Denmark': 76.17, 'Bahamas, The': 0.0, \
    'Greece': 54.64, 'Moldova': 0.0, 'Georgia': 0.0, \
    'China': 61.56,'Czech Republic': 75.48, 'Philippines': 68.46}
    data.Country = data.Country.apply(lambda x: socialized[x] if x in socialized.keys() else 0.0)
    return data


def _treatment(data):
    data.treatment = data.treatment.apply(lambda x: 1 if x == 'Yes' else 0)
    return data


def _remote_work(data):
    data.remote_work = data.remote_work.apply(lambda x: 1 if x == 'Yes' else 0)
    return data


def _family_hist(data):
    data.family_history = data.family_history.apply(lambda x: 1 if x == 'Yes' else 0)
    return data


def _work_interference(data):
    data.family_history = data.family_history.apply(lambda x: 4 if x == 'Often' else 3 if x == 'Sometimes' else 2 if x == 'Rarely' else 1 if x == 'Never' else 0)
    return data



def _employ(data):
    data.family_history = data.family_history.apply(lambda x: 25 if x == '6-25' else 5 if x == '1-5' else 100 if x == '26-100' else 500 if x == '100-500' else 1000 if x == '500-1000' else 2000)
    return data


def _leave(data):
    data.family_history = data.family_history.apply(lambda x: 1 if x == 'Very easy' else 2 if x == 'Somewhat easy' else 4 if x == 'Somewhat difficult' else 5 if x == 'Very difficult' else 3)
    return data

def clean_data(data):
    data = _gender_category(data)
    data = _tech(data)
    data = _drop_(data)
    data = _check_for_socialized_healthcare(data)
    data = _treatment(data)
    data = _remote_work(data)
    data = _family_hist(data)
    data = _work_interference(data)
    data = _employ(data)
    data = _leave(data)
    return data


def supervisor(data):
    data.supervisor = data.supervisor.apply(lambda x: 1 if x == 'Yes' else 0 if x == 'No' else 2)
    return data


if __name__ == '__main__':
    data = pd.read_csv('survey.csv')
    data = clean_data(data)
    print(data.head(10))
