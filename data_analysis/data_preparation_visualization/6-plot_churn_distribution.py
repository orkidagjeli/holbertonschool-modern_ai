#!/usr/bin/env python3
"""
Plot churn class distribution
"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """
    Plots a bar chart of the Churn value counts.

    Args:
        df: pandas DataFrame with a Churn column

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    counts = df['Churn'].value_counts()
    counts = counts.reindex(['No', 'Yes'])

    plt.bar(counts.index, counts.values, color=['skyblue', 'salmon'])
    plt.title('Churn Distribution')
    plt.ylabel('Count')

    plt.show()
