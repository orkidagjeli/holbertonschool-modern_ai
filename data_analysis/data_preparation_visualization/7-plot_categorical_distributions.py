#!/usr/bin/env python3
"""
Plot categorical feature distributions
"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """
    Plots a bar chart of value counts for each categorical column.

    Args:
        df: pandas DataFrame
        columns_to_plot: optional list of categorical columns. Defaults to
            all object columns except the target 'Churn'.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns = [c for c in df.select_dtypes(include='object').columns
                   if c != 'Churn']
    else:
        columns = list(columns_to_plot)

    n_cols = 3
    n_rows = (len(columns) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    for ax, col in zip(axes, columns):
        counts = df[col].value_counts()
        ax.bar(counts.index.astype(str), counts.values)
        ax.set_title(col)
        ax.tick_params(axis='x', rotation=45)

    # hide any unused subplots in the last row
    for ax in axes[len(columns):]:
        ax.set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
