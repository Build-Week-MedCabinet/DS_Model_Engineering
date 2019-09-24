"""
<<<<<<< HEAD
This library interfaces with the pickled engine.
=======
This library interfaces with the pickled model.
>>>>>>> django-app

Using predictor:
"""

import pickle
<<<<<<< HEAD
import os

=======
import pandas as pd
import os

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

import spacy
from spacy.tokenizer import Tokenizer
>>>>>>> django-app

##################
##SET PARAMETERS##
##################
params = {
<<<<<<< HEAD
    'engine': 'knn_02.pkl',
=======
    'model': 'knn_02.pkl',
>>>>>>> django-app
    'vectorizer': 'vectorizer_02.pkl'
}


<<<<<<< HEAD
def get_engine_path(**kwargs):
    return os.path.abspath(params['engine'])


def get_vectorizer_path(**kwargs):
    return os.path.abspath(params['vectorizer'])

=======
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
        vinput = self.vectorizer.transform(
            pd.DataFrame(
                pd.series(raw_input).to_dense()
            )
        )
        self.vectorized_input = vinput
        return vinput

    def predict(self, vectorized_input=None, size=5):
        # Check if any data available for prediction
        if vectorized_input is None and self.vectorized_input is None:
            raise NoDataProvided
        elif vectorized_input is None:
            vinput = self.vectorized_input
        else:
            vinput = vectorized_input

        # If data available, use model to get 'size' number of predictions
        results = self.model.kneighbors([vinput][0], n_neighbors=size)[1][0].tolist()
        return results


class Error(Exception):
    """Base class for Custom Errors"""
    pass


class NoDataProvided(Error):
    """No Data Provided"""
    pass


def get_abs_path(filename, **kwargs):
    return os.path.abspath(filename)
>>>>>>> django-app

