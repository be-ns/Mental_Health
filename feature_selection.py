from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import f1_score as f1
from data_cleaning import clean_data as cd
import pandas as pd
from sklearn.decomposition import PCA as pca
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier as kn_n
from sklearn.svm import SVC as sv_c
from sklearn.ensemble import GradientBoostingClassifier as gbc


def _train_test(data, preprocess):
    y = data.treatment
    data.drop(['treatment'], axis = 1, inplace = True)
    X = data
    if preprocess == 1:
        X = StandardScaler().fit_transform(X)
    x_tr, x_te, y_tr, y_te = tts(X, y)
    return x_tr, x_te, y_tr, y_te

def _score_model(pred, true):
    print(f1(true, pred))

def _build_r_forest(x_tr, x_te, y_tr, y_te):
    forest = rfc(n_estimators=1000, n_jobs=-1, verbose=1, class_weight="balanced")
    forest.fit(x_tr, y_tr)
    predicted = forest.predict(x_te)
    _score_model(predicted, y_te)
    zipped = zip(data.columns.tolist(), forest.feature_importances_)
    for x in list(sorted(zipped, key=lambda x: x[1])):
        print(x)

def _build_knn(x_tr, x_te, y_tr, y_te):
    knn = kn_n(n_neighbors = 3)
    knn.fit(x_tr, y_tr)
    predicted = knn.predict(x_te)
    _score_model(predicted, y_te)

def _build_svm(x_tr, x_te, y_tr, y_te):
    svm = sv_c(C=1, kernel = 'linear')
    svm.fit(x_tr, y_tr)
    predicted = svm.predict(x_te)
    _score_model(predicted, y_te)


def build_model(data):
    print('starting Random Forest')
    _build_r_forest(_train_test(data, preprocess = 0))
    print('starting KNN')
    _build_knn(_train_test(cd(pd.read_csv('survey.csv')), preprocess = 1))
    print('starting SVM')
    _build_svm(_train_test(cd(pd.read_csv('survey.csv')), preprocess=1))


if __name__ == '__main__':
    build_model(cd(pd.read_csv ('survey.csv')))
