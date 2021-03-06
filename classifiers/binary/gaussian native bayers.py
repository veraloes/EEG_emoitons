from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score


features_raw = pd.read_csv('../data_nan_to_0_deleted_13_viarniace.csv')
valence_raw = pd.read_csv('../valence_values.csv')

features = np.array(features_raw)
valence = np.array(valence_raw)
valence_ravel = np.array(np.ravel(valence_raw))


Y_valence_train_rows = np.ravel((valence[56:451, :]))
X_features_train_rows = features[56:451, :]

true_features = features[0:56, :]
true_valence = valence[0:56, :]


# X_features_train_rows, true_features, Y_valence_train_rows, true_valence = train_test_split(features, valence, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_features_train_rows, Y_valence_train_rows).predict(true_features)

print("Number of mislabeled points out of a total %d points : %d"
      % (true_features.shape[0], (true_valence != y_pred).sum()))

y_true = true_valence


a = accuracy_score(y_true, y_pred)

print('end')