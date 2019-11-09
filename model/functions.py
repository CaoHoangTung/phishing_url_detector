import pickle
from sklearn.svm import SVC
from joblib import dump, load

# test unseen data
# lay sample hang thu3 trong phishing.csv
import pandas as pd
data = pd.read_csv('data/phishing.csv')
test = data.drop(['Result','index'],axis=1).iloc[2].values
test_2d = test.reshape(1, -1)

# Load pre-trained model
svclassifier = load('pre_model.joblib') 
y_pred_test = svclassifier.predict(test_2d)
print("X=%s, Predicted=%s" % (test_2d, y_pred_test[0]))


# class Function():
#     def check_vector(vec):
#         # vec = arr [30 phan tu]

#         # chay model
#         res = 1
#         return res