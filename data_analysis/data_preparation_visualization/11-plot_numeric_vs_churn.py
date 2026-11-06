#!/usr/bin/env python3
"""
Plot numeric feature distribution by churn
"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Plots histograms of a numeric column for Churn=No and Churn=Yes.

    Args:
        df: pandas DataFrame with a Churn column
        col: numeric column name

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    no = df.loc[df['Churn'] == 'No', col]
    yes = df.loc[df['Churn'] == 'Yes', col]

    plt.hist([no, yes], bins=30, label=['No', 'Yes'])
    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    plt.legend(title='Churn')

    plt.show()
