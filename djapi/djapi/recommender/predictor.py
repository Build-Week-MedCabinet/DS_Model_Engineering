"""
This library interfaces with the pickled model.

Using predictor:
"""

import pickle
import os

import pandas as pd
import os
# model and vectorizer requirements
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
import spacy
from spacy.tokenizer import Tokenizer
# caching libraries and utility functions
from django.core.cache import cache
from djapi.recommender.caching import cache_file

##################
##SET PARAMETERS##
##################
params = {
    'model': 'knn_05.pkl',
    'vectorizer': 'vectorizer_05.pkl',
    'clean_data': 'cannabis_02.csv',
}


###################
##BUILD PREDICTOR##
###################
class Predictor():
    def __init__(self, model=None, vectorizer=None):
        self.model = load_file('model')
        self.vectorizer = load_file('vectorizer')

    def transform(self, raw_input):
        self.raw_input = raw_input
        vinput = pd.DataFrame(
            self.vectorizer.transform(
                pd.Series(raw_input)
            ).todense()
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

    def get_recommendation(self, size=5):
        strain_frame = pd.read_csv(
            get_abs_path(params['clean_data'])
        )
        rec_df = strain_frame.iloc[self.predict(size=size)]
        return rec_df.to_json(orient='records')


class Error(Exception):
    """Base class for Custom Errors"""
    pass


class NoDataProvided(Error):
    """No Data Provided"""
    pass


def get_abs_path(filename, **kwargs):
    if os.path.isfile(os.path.abspath(filename)):
        return os.path.abspath(filename)
    else:
        return os.path.join(
            os.getcwd(), 'djapi/recommender/'+filename,
        )


def get_file(file_key):
    if cache_file(file_key):
        return cache.get(file_key)
    else:
        cache_file(file_key, load_file(file_key))

    return cache.get(file_key)


def load_file(file_key):
    with open(get_abs_path(params[file_key]), 'rb') as f:
        opened = pickle.load(f)
    return opened
