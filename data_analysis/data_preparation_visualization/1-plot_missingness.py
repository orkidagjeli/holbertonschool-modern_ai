#!/usr/bin/env python3
"""
Visualize missing values in a DataFrame.
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Plot missing values in a DataFrame.
    """
    plt.figure(figsize=(12, 8))

    df = df.drop(columns=['customerID'], errors='ignore')
    missing = df.isnull()
    rows, cols = np.where(missing)

    plt.scatter(rows, cols, marker='|')
    plt.yticks(range(len(df.columns)), df.columns)
    plt.title('Missingness Plot')

    plt.tight_layout()
    plt.show()
