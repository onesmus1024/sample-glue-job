import pandas as pd


# simulate ETL process

# extract

def extract():
    return pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})


# transform

def transform(df):
    df['c'] = df['a'] + df['b']
    return df


# load

def load(df):
    df.to_csv('data.csv', index=False)




