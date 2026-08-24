import pandas as pd

def fill_missing_median(df, columns):
    """
    Fill missing values in selected numeric columns with the column median.
    """
    df = df.copy()

    for col in columns:
        df[col] = df[col].fillna(df[col].median())

    return df

def drop_missing(df, threshold=0.5):
    """
    Drop rows whose proportion of missing values is greater than threshold.
    """
    df = df.copy()

    missing_ratio = df.isna().mean(axis=1)
    df = df[missing_ratio <= threshold]

    return df

def normalize_data(df, columns):
    """
    Normalize selected numeric columns to the 0-1 range.
    """
    df = df.copy()

    for col in columns:
        min_val = df[col].min()
        max_val = df[col].max()

        if max_val != min_val:
            df[col] = (df[col] - min_val) / (max_val - min_val)

    return df