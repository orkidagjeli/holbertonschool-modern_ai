#!/usr/bin/env python3
"""Creates a linear regression model."""

from sklearn import linear_model


def Linear_Regression():
    """Creates and returns an untrained LinearRegression model."""
    model = linear_model.LinearRegression()
    return model
