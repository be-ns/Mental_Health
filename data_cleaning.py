import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = pd.read_csv('survey.csv')
    print(data.head(10))
