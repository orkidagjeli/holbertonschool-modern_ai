#!/usr/bin/env python3
"""
Scale numeric features
"""
from sklearn import preprocessing


def scale_numeric(df):
    """
    Standardizes MonthlyCharges and TotalCharges (mean=0, std=1).

    Args:
        df: pandas DataFrame

    Returns:
        The modified DataFrame
    """
    df = df.copy()

    cols = ['MonthlyCharges', 'TotalCharges']
    scaler = preprocessing.StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])

    return df
