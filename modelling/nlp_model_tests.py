import unittest
import warnings
from nlp_module import nlp_model

class nlp_model_test(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', category=ImportWarning)

    def test_load(self):
        predictor = nlp_model.Predictor()
        self.assertIsNotNone(predictor)

    def test_transform(self):
        predictor = nlp_model.Predictor()
        self.assertIsNotNone(predictor.transform('some random text to transform'))


if __name__ == "__main__":
    unittest.main()