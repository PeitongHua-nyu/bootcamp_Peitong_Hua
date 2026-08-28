import numpy as np
import pandas as pd


def add_spend_income_ratio(df):
    df = df.copy()
    df['spend_income_ratio'] = df['spend'] / df['income']
    return df


def add_spend_per_transaction(df):
    df = df.copy()
    df['spend_per_transaction'] = (
        df['spend'] / df['transactions'].replace(0, np.nan)
    )
    return df


def one_hot_encode_region(df):
    df = df.copy()
    return pd.get_dummies(df, columns=['region'], prefix='region')