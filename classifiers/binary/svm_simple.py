from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


features_raw = pd.read_csv('L1_dataset.csv')
valence_raw = pd.read_csv('../valence_values.csv')

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = valence[56:451, :]
# valence_train_rows_selected = valence_raw.iloc[[1],[3, 4, 5, 7, 8, 12, 13, 14, 15, 17, 18, 43, 44]]
train_rows = features[56:451, :]
true_features = features[0:56, :]
true_valence = valence[0:56, :]

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import svm

# clf = svm.SVC()

C = 1  # SVM regularization parameter
# clf = svm.SVC(kernel='linear', C=C)
clf = svm.LinearSVC()
# clf = svm.SVC(kernel='rbf', gamma=0.7, C=C)
# clf = svm.SVC(kernel='poly', degree=3, gamma='auto', C=C)

# clf = tree.DecisionTreeClassifier()
clf.fit(train_rows, valence_train_rows)
result = clf.predict(true_features)

print("True = ",true_valence)
print("Estimated = ", result)

y_pred = result
y_true = true_valence

a = accuracy_score(y_true, y_pred)



print(a)

print("done")
