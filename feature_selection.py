from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import f1_score as f1
from data_cleaning import clean_data as cd
import pandas as pd


def _train_test(X, y):
    x_tr, x_te, y_tr, y_te = tts(X, y)
    return x_tr, x_te, y_tr, y_te

def _score_model(pred, true):
    print(f1(true, pred))

def build_model(data):
    y = data.treatment
    data.drop(['treatment'], axis = 1, inplace = True)
    X = data[['wellness_program','Gender','phys_health_interview','mental_health_consequence', 'supervisor', 'care_options', 'no_employees','Country', 'family_history', 'Age', 'work_interfere']]
    x_tr, x_te, y_tr, y_te = _train_test(X, y)
    forest = rfc(n_estimators=10000,n_jobs=-1, verbose=1, class_weight="balanced")
    forest.fit(x_tr, y_tr)
    predicted = forest.predict(x_te)
    _score_model(predicted, y_te)
    zipped = zip(data.columns.tolist(), forest.feature_importances_)
    for x in list(sorted(zipped, key=lambda x: x[1])):
        print(x)


if __name__ == '__main__':
    build_model(cd(pd.read_csv('survey.csv')))
