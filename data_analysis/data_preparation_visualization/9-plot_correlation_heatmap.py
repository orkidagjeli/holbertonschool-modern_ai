#!/usr/bin/env python3
"""
Plot a correlation heatmap.
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Generate an annotated correlation heatmap.
    """
    plt.figure(figsize=(6, 5))

    numeric_cols = df.select_dtypes(include='number').columns

    continuous_cols = [
        col for col in numeric_cols
        if df[col].nunique() > 2
    ]

    correlation = df[continuous_cols].corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap='coolwarm',
        vmin=-1,
        vmax=1
    )

    plt.title('Correlation Matrix')
    plt.show()
