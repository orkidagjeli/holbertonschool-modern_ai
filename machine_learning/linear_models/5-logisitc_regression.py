#!/usr/bin/env python3
"""Creates a Logistic Regression model."""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Creates and returns an untrained Logistic Regression model."""
    model = linear_model.LogisticRegression(random_state=random_state)
    return model
