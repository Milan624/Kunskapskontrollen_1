import pandas as pd
import sqlite3

df = pd.read_csv(r"C:\Users\milan\Documents\TUC\Data_science\index.csv")
df.groupby("coffee_name")["money"].agg(sum)
df
latte_df = df[df['coffee_name'] == 'Latte']
print(latte_df)

df['coffee_name'] = df['coffee_name'].replace('Hot Chocolate', 'Cold Chocolate')



print(df['coffee_name'].unique())
df
import pandas as pd

def replace_coffee_name(df):
    """
    >>> df = pd.DataFrame({'coffee_name': ['Hot Chocolate', 'Latte', 'Hot Chocolate']})
    >>> replace_coffee_name(df)
    >>> df['coffee_name'].tolist()
    ['Cold Chocolate', 'Latte', 'Cold Chocolate']
    """
    df['coffee_name'] = df['coffee_name'].replace('Hot Chocolate', 'Cold Chocolate')

import pandas as pd
import doctest

def replace_coffee_name(df):
    """
    Ersätter 'Hot Chocolate' med 'Cold Chocolate' i kolumnen 'coffee_name'.

    >>> df = pd.DataFrame({'coffee_name': ['Hot Chocolate', 'Latte', 'Hot Chocolate']})
    >>> replace_coffee_name(df)
    >>> df['coffee_name'].tolist()
    ['Cold Chocolate', 'Latte', 'Cold Chocolate']
    """
    df['coffee_name'] = df['coffee_name'].replace('Hot Chocolate', 'Cold Chocolate')

if __name__ == "__main__":
    result = doctest.testmod()
    print(result)

