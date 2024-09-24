import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import xgboost as xgb

# Load dataset
dataset_path  = 'D:/Github/AIO-exercise/Module_3/Week5_Xgboost/data/Problem4.csv'
df = pd.read_csv(dataset_path)

#Split dataset
X = df.drop('Target', axis = 1)
y = df['Target']

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 7)

#Training
xg_clf = xgb.XGBClassifier(seed = 7)

xg_clf.fit(X_train, y_train)

#Predict
y_pred = xg_clf.predict(X_test)

#Evaluate
print(accuracy_score(y_train,xg_clf.predict(X_train)))
print(accuracy_score(y_test, y_pred))