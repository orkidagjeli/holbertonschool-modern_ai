#!/usr/bin/env python3
"""Perform Chi-square tests on categorical features."""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Calculate Chi-square p-values for categorical features against Churn."""

    results = {}

    for column in df.columns:
        if column == 'Churn':
            continue

        if df[column].dtype == 'object' or df[column].nunique() <= 10:
            contingency_table = pd.crosstab(df[column], df['Churn'])

            chi2, p_value, dof, expected = stats.chi2_contingency(
                contingency_table
            )

            results[column] = p_value

    return results
