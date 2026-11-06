#!/usr/bin/env python3
"""
Plot churn rate per category
"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """
    Plots the churn rate (proportion of 'Yes') for each category of a column.

    Args:
        df: pandas DataFrame with a Churn column
        col: categorical column name

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    churn_rate = (df['Churn'] == 'Yes').groupby(df[col]).mean()

    plt.bar(churn_rate.index.astype(str), churn_rate.values)
    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)

    plt.show()
