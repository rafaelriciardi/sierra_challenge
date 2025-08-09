import unittest
import json
from solution import check_spam

with open('test_cases.json', encoding='utf-8') as test_file:
    test_cases = json.load(test_file)

class TestClassifications(unittest.TestCase):

    def test_case_0(self):
        response = check_spam(test_cases[0]['content'])
        self.assertEqual(response['is_spam'], test_cases[0]['is_spam'], 'Classification error')
    
    def test_case_1(self):
        response = check_spam(test_cases[1]['content'])
        self.assertEqual(response['is_spam'], test_cases[1]['is_spam'], 'Classification error')

    def test_case_2(self):
        response = check_spam(test_cases[2]['content'])
        self.assertEqual(response['is_spam'], test_cases[2]['is_spam'], 'Classification error')

    def test_case_3(self):
        response = check_spam(test_cases[3]['content'])
        self.assertEqual(response['is_spam'], test_cases[3]['is_spam'], 'Classification error')

    def test_case_4(self):
        response = check_spam(test_cases[4]['content'])
        self.assertEqual(response['is_spam'], test_cases[4]['is_spam'], 'Classification error')

if __name__ == '__main__':
    unittest.main()