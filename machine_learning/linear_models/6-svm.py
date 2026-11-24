#!/usr/bin/env python3
"""Creates SVM classifiers with different kernels."""

from sklearn import svm


def get_SVM_model(name, random_state):
    """Creates and returns an untrained SVM classifier."""
    model = svm.SVC(kernel=name, random_state=random_state)
    return model
