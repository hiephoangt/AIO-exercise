import pandas as pd
import numpy as np

data = pd.read_csv("Module_2/Week4_Statistics/data/advertising.csv")

# Question 5:


def correlation(X, Y):
    return np.corrcoef(x, y)[0][1]


x = data['TV']
y = data['Radio']

corr_xy = correlation(x, y)
print(f" Correlation between TV and Sales : { round(corr_xy , 2)}")

# Question 6:
features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(
            f" Correlation between { feature_1 } and { feature_2 }: {round (correlation_value , 2)}")

#Question 7:
x = data['Radio']
y = data['Newspaper']
result = np.corrcoef(x, y)
print(result)

# Question 8:
print(data.corr())

# Question 9:
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,8))
sns.heatmap(data.corr(), annot=True, fmt='.2f', linewidths=.5)
plt.show()