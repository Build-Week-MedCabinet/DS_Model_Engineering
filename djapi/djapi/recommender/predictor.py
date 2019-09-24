"""
This library interfaces with the pickled engine.

Using predictor:
"""

import pickle
import os


##################
##SET PARAMETERS##
##################
params = {
    'engine': 'knn_02.pkl',
    'vectorizer': 'vectorizer_02.pkl'
}


def get_engine_path(**kwargs):
    return os.path.abspath(params['engine'])


def get_vectorizer_path(**kwargs):
    return os.path.abspath(params['vectorizer'])


