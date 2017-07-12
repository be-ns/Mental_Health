from sklearn.ensemble import RandomForestClassifier
from data_cleaning import clean_data as cd
import pandas as pd


if __name__ == '__main__':
    data = cd(pd.read_csv('survey.csv'))
    print(data.head(10))
