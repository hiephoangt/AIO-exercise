import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

dataset_path = 'Module_3/Week4_Ensemble_Learning/data/Housing.csv'
df = pd.read_csv(dataset_path)

#Data Preprocessing
categories_columns = df.select_dtypes(include=['object']).columns.tolist()
print(categories_columns)

#encoder data
ordinal_encoder = OrdinalEncoder()
encoder_ordinal_cols = ordinal_encoder.fit_transform(df[categories_columns])
encoder_categories_df = pd.DataFrame(encoder_ordinal_cols, columns=categories_columns)
numarical_df = df.drop(categories_columns, axis=1)
encoder_df = pd.concat([numarical_df,encoder_categories_df],axis = 1)

#normalize data
nomalizer = StandardScaler()
dataset_arr = nomalizer.fit_transform(encoder_df)

#split dataset
X,y = dataset_arr[:,1:],dataset_arr[:,0]
test_size = 0.3
random_state = 1
is_shuffer = True
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size,random_state=random_state,shuffle=is_shuffer)

#train model
random_forest_model = RandomForestRegressor(random_state=random_state)
random_forest_model.fit(X_train,y_train)

adaboost_model = AdaBoostRegressor(random_state=random_state)
adaboost_model.fit(X_train,y_train)

gradient_boosting_model = GradientBoostingRegressor(random_state=random_state)
gradient_boosting_model.fit(X_train,y_train)

#predict
y_pre = random_forest_model.predict(X_test)
mae = mean_absolute_error(y_test,y_pre)
mse = mean_squared_error(y_test,y_pre)
print('Random forest model:')
print(f'\t\tMAE: {mae}')
print(f'\t\tMSE: {mse}')

y_pre = adaboost_model.predict(X_test)
mae = mean_absolute_error(y_test,y_pre)
mse = mean_squared_error(y_test,y_pre)
print('Adaboost model:')
print(f'\t\tMAE: {mae}')
print(f'\t\tMSE: {mse}')

y_pre = gradient_boosting_model.predict(X_test)
mae = mean_absolute_error(y_test,y_pre)
mse = mean_squared_error(y_test,y_pre)
print('Gradient boosting model:')
print(f'\t\tMAE: {mae}')
print(f'\t\tMSE: {mse}')