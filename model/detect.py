import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from mlxtend.plotting import plot_decision_regions
from sklearn import datasets
from pandas.plotting import scatter_matrix

data = pd.read_csv('data/phishing.csv')
print(data.head())
X = data.drop('index',axis=1).iloc[:, :30]
y = data.iloc[:,-1]
print(X)
print(y)

# scatter_matrix(X, alpha=0.2, figsize=(6, 6), diagonal='kde')
# plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
# print(X_test)
print("test : \n", X_test)
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)


y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(y_pred)

