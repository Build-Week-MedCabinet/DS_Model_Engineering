"""
This library interfaces with the pickled model.

Using predictor:
"""

import pickle
import pandas as pd
import os


##################
##SET PARAMETERS##
##################
params = {
    'model': 'knn_02.pkl',
    'vectorizer': 'vectorizer_02.pkl'
}


###################
##BUILD PREDICTOR##
###################
class Predictor():
    def __init__(self, model, vectorizer):
        self.model = pickle.load(open(
            get_abs_path(params['model']), 'rb',
        ))
        self.vectorizer = pickle.load(open(
            get_abs_path(params['vectorizer']), 'rb',
        ))

    def transform(self, raw_input):
        self.raw_input = raw_input
        self.vectorized_input = self.vectorizer.transform(
            pd.DataFrame(
                pd.series(raw_input).to_dense()
            )
        )

    def predict(self, vectorized_input=None, size=5):
        # Check if any data available for prediction
        if vectorized_input is None and self.vectorized_input is None:
            raise NoDataProvided

        # If data available, use model to get 'size' number of predictions


        return self.vectorized_input


class Error(Exception):
    """Base class for Custom Errors"""
    pass


class NoDataProvided(Error):
    """No Data Provided"""
    pass


def get_abs_path(filename, **kwargs):
    return os.path.abspath(filename)

