#!/usr/bin/env python3
"""
Feature engineering: NumServices and TenureGroup
"""
import pandas as pd


def create_features(df):
    """
    Creates NumServices and TenureGroup, then drops the columns used.

    Args:
        df: pandas DataFrame

    Returns:
        The modified DataFrame
    """
    df = df.copy()

    service_cols = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup',
                    'DeviceProtection', 'TechSupport', 'StreamingTV',
                    'StreamingMovies']

    # each 'Yes' counts as one service
    df['NumServices'] = (df[service_cols] == 'Yes').sum(axis=1)
    # internet counts when it is DSL or Fiber optic
    df['NumServices'] += df['InternetService'].isin(
        ['DSL', 'Fiber optic']).astype(int)

    # upper bounds inclusive, 0 excluded (it falls outside the first bin)
    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'])

    df = df.drop(columns=service_cols + ['InternetService', 'tenure'])
    return df
