#!/usr/bin/env python3
"""
Clean missing TotalCharges values
"""


def clean_total_charges(df, method='drop'):
    """
    Handles missing values in the TotalCharges column.

    Args:
        df: pandas DataFrame with missing values in TotalCharges
        method: 'drop', 'median' or 'impute'

    Returns:
        The modified DataFrame (a copy, the input is left untouched)
    """
    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['TotalCharges'].median())
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure'])

    return df
