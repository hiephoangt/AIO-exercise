import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Module_3/Week1_Pandas/data/IMDB-Movie-Data.csv')
print(df.head(5))

# Understand some basic information about the data
print(df.info())
print(df.describe())

# Data Selection – Indexing and Slicing data
genre = df['Genre']  # Tách cột thánh Series, để tách thành Df: df[['Genre]]
print(genre.head())

# tách cùng lúc nhiều cột
some_cols = df[['Title', 'Genre', 'Actors', 'Director', 'Rating']]
df.iloc[10:15][['Title', 'Genre', 'Actors', 'Director', 'Rating']]  # tách hàng

# Data Selection – Based on Conditional filtering:
df[((df['Year'] >= 2010) & (df['Year'] <= 2015))
    & (df['Rating'] < 6.0)
    & (df['Revenue (Millions)'] > df['Revenue (Millions)'].quantile(0.95))]

# Groupby Operations:
df.groupby('Director')[['Rating']].mean().head()

# Sorting Operations:
df.groupby('Director')[['Rating']].mean().sort_values(
    ['Rating'], ascending=False).head()

# View missing values:
df.isnull().sum()

# Deal with missing values - Deleting:
df.drop('Metascore', axis=1).head()
df.dropna()

# Dealing with missing values - Filling:
revenue_mean = df['Revenue (Millions)'].mean()
print("The mean revenue is: ", revenue_mean)
df['Revenue (Millions)'].fillna(revenue_mean, inplace=True)

# apply() functions:


def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'


df['Rating_category'] = df['Rating'].apply(rating_group)
df[['Title', 'Director', 'Rating', 'Rating_category']].head(5)
