import pandas as pd
import numpy as np


def _gender_category(data):
    male = ['male', 'm', 'mal','make', 'man', 'guy', 'mail', 'male-ish', 'maile', 'male (cis)', 'cis male']
    female = ['female', 'femake', 'femail', 'cis-female/femme', 'female ', 'woman', 'girl']
    data.Gender = data.Gender.apply(lambda x: 1 if x.lower() in male else 2 if x.lower() in female else 3)
    return data


def _drop_(data):
    data.drop_columns(['comments', 'Timestamp', 'state', 'self_employed'])


def _tech(data):
    data.tech_company = data.tech_company.apply(lambda x: 1 if x == 'Yes' else 0)
    return data


def clean_data(data):
    data = _gender_category(data)
    data = _tech(data)
    data = _drop_(data)
    return data

if __name__ == '__main__':
    data = pd.read_csv('survey.csv')
    data = clean_data(data)
    print(data.head(10))
