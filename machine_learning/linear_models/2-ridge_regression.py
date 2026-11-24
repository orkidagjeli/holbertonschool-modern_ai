#!/usr/bin/env python3
"""Creates a Ridge Regression model."""

from sklearn import linear_model


def ridge_regression(random_state):
    """Creates and returns an untrained Ridge regression model."""
    model = linear_model.Ridge(random_state=random_state)
    return model
