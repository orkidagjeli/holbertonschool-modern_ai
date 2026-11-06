#!/usr/bin/env python3
"""Perform Welch's t-tests on numeric features."""

from scipy import stats


def ttest_numeric(df):
    """Calculate Welch's t-test p-values for numeric features."""

    results = {}

    numeric_columns = df.select_dtypes(include='number').columns

    churn_yes = df[df['Churn'] == 'Yes']
    churn_no = df[df['Churn'] == 'No']

    for column in numeric_columns:
        if column == 'Churn':
            continue

        t_stat, p_value = stats.ttest_ind(
            churn_yes[column].dropna(),
            churn_no[column].dropna(),
            equal_var=False
        )

        results[column] = p_value

    return results
