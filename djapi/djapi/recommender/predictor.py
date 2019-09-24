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
    def __init__(self, engine, vectorizer):
        self.engine = pickle.load(open(
            get_abs_path(params['model']), 'rb',
        ))
        self.vectorizer = pickle.load(open(
            get_abs_path(params['vectorizer']), 'rb',
        ))

    def transform_inputs(self, raw_input):
        self.raw_input = raw_input
        self.vectorized_input = self.vectorizer.transform(
            pd.DataFrame(
                pd.series(raw_input).to_dense()
            )
        )



def get_abs_path(filename, **kwargs):
    return os.path.abspath(filename)

