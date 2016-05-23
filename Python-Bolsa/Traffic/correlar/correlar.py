from __future__ import division
import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from scipy.stats.stats import pearsonr
from scipy import stats
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
from sklearn.svm import SVR
from sklearn.grid_search import GridSearchCV
from sklearn.learning_curve import learning_curve
from sklearn.kernel_ridge import KernelRidge
from sklearn import datasets, neighbors, linear_model
from sklearn import svm
from sklearn.metrics import jaccard_similarity_score
from sklearn.metrics import accuracy_score

data = pd.read_csv('2014-MIDAS-Site 237-LM934.csv')

data.describe()
data.columns[1:]

speed = (data[' Speed Value']).values
flow = (data[' Total Carriageway Flow']).values

print (speed.shape[0])
dimensionAnalisis = 500
speed = speed[1:dimensionAnalisis]
flow = flow[1:dimensionAnalisis]

r = np.corrcoef(speed, flow)
print ("Coeficiente de Correlacion " + str(r[1][0]))

# Entrenamiento
n_samples = len(speed)
porcentaje_samples = .75

X_train = np.random.random_sample((2,porcentaje_samples * n_samples))
X_train[0] = speed[:porcentaje_samples * n_samples]
X_train[1] = speed[:porcentaje_samples * n_samples]
X_train = X_train.T
y_train = flow[:porcentaje_samples * n_samples]

X_test = np.random.random_sample((2,(1-porcentaje_samples) * n_samples + 1))
X_test[0] = speed[porcentaje_samples * n_samples:]
X_test[1] = speed[porcentaje_samples * n_samples:]
X_test = X_test.T
y_test = flow[porcentaje_samples * n_samples:]

print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)

knn = neighbors.KNeighborsClassifier()
logistic = linear_model.LogisticRegression()
clf = svm.SVR()
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)

print('Num Samples: %d' % n_samples)
print('Porcentaje Samples: %f' % porcentaje_samples)
#print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))
#print('LogisticRegression score: %f'  % logistic.fit(X_train, y_train).score(X_test, y_test))
print('SVR score: %f' % clf.fit(X_train, y_train).score(X_test, y_test))
print('SVR RBF score: %f' % svr_rbf.fit(X_train, y_train).score(X_test, y_test))
print('SVR POLY score: %f' % svr_poly.fit(X_train, y_train).score(X_test, y_test))

