"""
This library interfaces with the pickled model.

Using predictor:
"""

# Path and File Libraries
import os
import pickle
# Data Transformation Libraries
import pandas as pd
import numpy as np
import spacy
from spacy.tokens import Doc

# Initialize parameters and spacy from __init__.py
from nlp_module import params, nlp


###################
##BUILD PREDICTOR##
###################
class Predictor():
    def __init__(self, model=None, vectorizer=None):
        self.model = load_file('model')
        self.vectorizer = Vectorizer()

    def transform(self, raw_input):
        self.raw_input = raw_input
        vinput = self.vectorizer.transform(raw_input)
        self.vectorized_input = vinput # Store vinput
        return vinput

    def predict(self, vectorized_input=None, size=5):
        # If data available, use model to get 'size' number of predictions
        if self.data_available(vectorized_input):
            results = self.model.query(self.vectorized_input, n_neighbors=size)[1][0].tolist()
            return results
        else:
            raise Error

    def data_available(self, vectorized_input):
        if vectorized_input is None and self.vectorized_input is None:
            raise NoDataProvided
        elif self.vectorized_input is None:
            return False
        else:
            self.vectorized_input = vectorized_input
            return True


class Vectorizer():
    def __init__(self):
        pass

    def transform(self, input_string):
        vectorized_input = get_vector_from_doc(
            tokenize_text(input_string)
        )
        return vectorized_input.reshape(1,-1)


####################
###Error Handling###
####################
class Error(Exception):
    """Base class for Custom Errors"""
    pass


class NoDataProvided(Error):
    """No Data Provided"""
    pass

######################
###Helper Functions###
######################
def get_abs_path(filename, **kwargs):
    if os.path.isfile(os.path.abspath(filename)):
        return os.path.abspath(filename)
    else:
        return os.path.join(
            os.getcwd(), 'djapi/recommender/'+filename,
        )


def load_file(file_key):
    with open(get_abs_path(params[file_key]), 'rb') as f:
        opened = pickle.load(f)
    return opened

############################
###Spacy filter/tokenizer###
############################

# Wrap filter/tokenizer
def filter_data(func):
    def wrapper(text):
        return filter_doc(func(text))
    return wrapper


# Filter on stop_words
def filter_doc(doc):
    filtered_sentence = []
    for word in doc:
        lexeme = doc.vocab[word.text]
        if lexeme.is_stop == False:
            if word.is_punct == False:
                filtered_sentence.append(word.text)
    return Doc(nlp.vocab, filtered_sentence,[True]*len(filtered_sentence))  # Use to return a spacy.tokens.Doc


@filter_data
def tokenize_text(text):
    return nlp(text)


def get_vector_from_doc(x):
    return x.vector