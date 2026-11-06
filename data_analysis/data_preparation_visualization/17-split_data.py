#!/usr/bin/env python3
"""
Split data into train and test sets
"""
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """
    Splits a DataFrame into stratified train and test sets.

    Args:
        df: pandas DataFrame
        target: name of the target column
        test_size: proportion of the data used for the test set
        random_state: random seed

    Returns:
        (X_train, X_test, y_train, y_test)
    """
    X = df.drop(columns=[target])
    y = df[target]

    return model_selection.train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y)
