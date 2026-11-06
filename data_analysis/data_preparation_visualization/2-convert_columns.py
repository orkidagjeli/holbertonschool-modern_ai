#!/usr/bin/env python3
"""
Convert column types
"""
import pandas as pd


def convert_columns(df):
    """
    Converts TotalCharges to numeric and maps SeniorCitizen to No/Yes.

    Args:
        df: pandas DataFrame containing TotalCharges and SeniorCitizen

    Returns:
        The modified DataFrame
    """
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})
    return df
