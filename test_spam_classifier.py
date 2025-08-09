import unittest
import json
from solution import SpamClassifier

with open('test_cases.json', encoding='utf-8') as test_file:
    test_cases = json.load(test_file)

model = SpamClassifier()

# Testing main model with real use cases
class TestClassifications(unittest.TestCase):
    def test_case_0(self):
        response = model.model_classifier(test_cases[0]['content'])
        self.assertEqual(response['is_spam'], test_cases[0]['is_spam'], 'Classification error')
    
    def test_case_1(self):
        response = model.model_classifier(test_cases[1]['content'])
        self.assertEqual(response['is_spam'], test_cases[1]['is_spam'], 'Classification error')

    def test_case_2(self):
        response = model.model_classifier(test_cases[2]['content'])
        self.assertEqual(response['is_spam'], test_cases[2]['is_spam'], 'Classification error')

    def test_case_3(self):
        response = model.model_classifier(test_cases[3]['content'])
        self.assertEqual(response['is_spam'], test_cases[3]['is_spam'], 'Classification error')

    def test_case_4(self):
        response = model.model_classifier(test_cases[4]['content'])
        self.assertEqual(response['is_spam'], test_cases[4]['is_spam'], 'Classification error')

# Testing fallback with real use cases
class TestFallbackClassifications(unittest.TestCase):
    def test_fallback_case_0(self):
        response = model.fallback_model_classifier(test_cases[0]['content'])
        self.assertEqual(response['is_spam'], test_cases[0]['is_spam'], 'Fallback Classification error')
    
    def test_fallback_case_1(self):
        response = model.fallback_model_classifier(test_cases[1]['content'])
        self.assertEqual(response['is_spam'], test_cases[1]['is_spam'], 'Fallback Classification error')

    def test_fallback_case_2(self):
        response = model.fallback_model_classifier(test_cases[2]['content'])
        self.assertEqual(response['is_spam'], test_cases[2]['is_spam'], 'Fallback Classification error')

    def test_fallback_case_3(self):
        response = model.fallback_model_classifier(test_cases[3]['content'])
        self.assertEqual(response['is_spam'], test_cases[3]['is_spam'], 'Fallback Classification error')

    def test_fallback_case_4(self):
        response = model.fallback_model_classifier(test_cases[4]['content'])
        self.assertEqual(response['is_spam'], test_cases[4]['is_spam'], 'Fallback Classification error')

# Testing prediction with real use cases
class TestPrediction(unittest.TestCase):
    def test_predict_case_0(self):
        response = model.predict(test_cases[0]['content'])
        self.assertEqual(response['is_spam'], test_cases[0]['is_spam'], 'Pedict Classification error')
    
    def test_predict_case_1(self):
        response = model.predict(test_cases[1]['content'])
        self.assertEqual(response['is_spam'], test_cases[1]['is_spam'], 'Pedict Classification error')

    def test_predict_case_2(self):
        response = model.predict(test_cases[2]['content'])
        self.assertEqual(response['is_spam'], test_cases[2]['is_spam'], 'Pedict Classification error')

    def test_predict_case_3(self):
        response = model.predict(test_cases[3]['content'])
        self.assertEqual(response['is_spam'], test_cases[3]['is_spam'], 'Pedict Classification error')

    def test_predict_case_4(self):
        response = model.predict(test_cases[4]['content'])
        self.assertEqual(response['is_spam'], test_cases[4]['is_spam'], 'Pedict Classification error')

if __name__ == '__main__':
    unittest.main()