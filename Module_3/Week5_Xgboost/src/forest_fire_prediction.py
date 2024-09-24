import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import xgboost as xgb
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

# Load datasets
dataset_path = 'D:/Github/AIO-exercise/Module_3/Week5_Xgboost/data/Problem3.csv'
data_df = pd.read_csv(dataset_path)

# Data preprocessing
categorial_cols = data_df.select_dtypes(include=['object', 'bool']).columns

for col in categorial_cols:
    n_categoricals = data_df[col].nunique()
    print(f'Number of categories in {col}: {n_categoricals}')

orinal_encoder = OrdinalEncoder()
encoder_categorical_cols = orinal_encoder.fit_transform(
    data_df[categorial_cols])
encoder_categorical_df = pd.DataFrame(
    encoder_categorical_cols,
    columns=categorial_cols
)

numarical_df = data_df.drop(categorial_cols, axis=1)
encoder_df = pd.concat([numarical_df, encoder_categorical_df], axis=1)

# Split data
X = encoder_df.drop('area', axis=1)
y = encoder_df['area']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=7)

# Train XGBoost model
xg_reg = xgb.XGBRegressor(
    seed=7,
    learning_rate=0.01,
    n_estimators=102,
    max_depth=3
)

xg_reg.fit(X_train, y_train)

# Predictions
preds = xg_reg.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, preds)
mse = mean_squared_error(y_test, preds)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
