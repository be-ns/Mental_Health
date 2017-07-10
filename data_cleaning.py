import pandas as pd
import numpy as np


def gender_category(data):
    male = ['male', 'm', 'mal','make', 'man', 'guy', 'mail', 'male-ish', 'maile', 'male (cis)', 'cis male']
    female = ['female', 'femake', 'femail', 'cis-female/femme', 'female ', 'woman', 'girl']
    data.Gender = data.Gender.apply(lambda x: 1 if x in male else 2 if x in female else 3)
    return data

if __name__ == '__main__':
    data = pd.read_csv('survey.csv')
    data = gender_category(data)
    print(data.Gender.head(12))
