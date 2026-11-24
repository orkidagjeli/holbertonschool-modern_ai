#!/usr/bin/env python3
"""Creates SHAP explanations for regression models."""

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Creates a SHAP explainer and calculates SHAP values."""
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)

    return explainer, shap_values
