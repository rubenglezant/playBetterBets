# http://scikit-learn.org/stable/auto_examples/exercises/digits_classification_exercise.html
# DataSET: http://scikit-learn.org/stable/auto_examples/datasets/plot_digits_last_image.html

print(__doc__)

from sklearn import datasets, neighbors, linear_model

digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

n_samples = len(X_digits)
porcentaje_samples = .55

X_train = X_digits[:porcentaje_samples * n_samples]
y_train = y_digits[:porcentaje_samples * n_samples]
X_test = X_digits[porcentaje_samples * n_samples:]
y_test = y_digits[porcentaje_samples * n_samples:]

knn = neighbors.KNeighborsClassifier()
logistic = linear_model.LogisticRegression()

print(digits)
print('Num Samples: %d' % n_samples)
print('Porcentaje Samples: %f' % porcentaje_samples)
print('KNN score: %f' % knn.fit(X_train, y_train).score(X_test, y_test))
print('LogisticRegression score: %f'
      % logistic.fit(X_train, y_train).score(X_test, y_test))
