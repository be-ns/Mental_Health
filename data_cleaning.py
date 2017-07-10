import pandas as pd
import numpy as np


def gender_category(data):
    male = ['male', 'm', 'mal','make', 'man', 'guy', 'mail', 'male-ish', 'maile', 'male (cis)', 'cis male']
    female = ['female', 'femake', 'femail', 'cis-female/femme', 'female ', 'woman', 'girl']

if __name__ == '__main__':
    data = pd.read_csv('survey.csv')
    print(data.head(10))
