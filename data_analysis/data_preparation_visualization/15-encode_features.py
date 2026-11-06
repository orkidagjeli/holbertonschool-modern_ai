#!/usr/bin/env python3
"""
Encode features for modeling
"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    Encodes the target, binary, categorical and tenure group columns.

    Args:
        df: pandas DataFrame

    Returns:
        df_encoded: the encoded DataFrame
        churn_le: fitted LabelEncoder for Churn
        binary_oe: fitted OrdinalEncoder for the binary columns
        tenure_oe: fitted OrdinalEncoder for TenureGroup
    """
    df = df.copy()

    # target: No -> 0, Yes -> 1
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    # binary columns: No -> 0, Yes -> 1, one shared single-feature encoder
    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling',
                   'SeniorCitizen']
    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    binary_oe.fit(df[['Partner']])
    for col in binary_cols:
        df[col] = binary_oe.transform(df[[col]]).astype(int).ravel()

    # tenure group: alphabetical order (the default for OrdinalEncoder)
    tenure_oe = preprocessing.OrdinalEncoder()
    df['TenureGroup'] = tenure_oe.fit_transform(
        df[['TenureGroup']]).astype(int)

    # one-hot, first category dropped, as 0/1 integers
    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True, dtype=int)

    return df, churn_le, binary_oe, tenure_oe
