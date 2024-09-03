import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

# Load the diabetes dataset
irisX,irisY = datasets.load_iris(return_X_y=True)

# Split train:test = 8:2
X_train,X_test,y_train,y_test = train_test_split(irisX,irisY,test_size=0.2,random_state = 42)

# Scale the features using StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build KNN Classifier
knn_classifier = KNeighborsClassifier(n_neighbors=3)
knn_classifier.fit(X_train,y_train)

# Predict on test set
y_pred = knn_classifier.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy}")

f1 = f1_score(y_test,y_pred,average='weighted')
print(f"F1 Score: {f1}")

precision = precision_score(y_test,y_pred,average='weighted')
print(f"Precision: {precision}")

recall = recall_score(y_test,y_pred,average='weighted')
print(f"Recall: {recall}")