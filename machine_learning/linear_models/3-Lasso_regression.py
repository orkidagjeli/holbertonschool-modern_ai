#!/usr/bin/env python3
"""Creates a Lasso Regression model."""

from sklearn import linear_model


def lasso_regression(random_state):
    """Creates and returns an untrained Lasso regression model."""
    model = linear_model.Lasso(random_state=random_state)
    return model
