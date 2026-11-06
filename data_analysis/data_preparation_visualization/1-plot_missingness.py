#!/usr/bin/env python3
"""
Missingness plot
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Plots missing values of a DataFrame as vertical bars.

    x-axis: row indices
    y-axis: column names

    Args:
        df: pandas DataFrame to analyze

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    xs = []
    ys = []
    for i, col in enumerate(df.columns):
        # positional row numbers where this column is null
        rows = np.where(df[col].isnull().to_numpy())[0]
        xs.extend(rows)
        ys.extend([i] * len(rows))

    plt.scatter(xs, ys, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title('Missingness Plot')

    plt.tight_layout()
    plt.show()
