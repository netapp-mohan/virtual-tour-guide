import unittest
from unittest.mock import patch
from utils import get_country, get_days

class TestUtils(unittest.TestCase):

    @patch('builtins.input', side_effect = ['Hungary'])
    def test_get_country(self, ex_inp):
        country = get_country()
        self.assertEqual(country, 'Hungary')

    @patch('builtins.input', side_effect = ['Hungry', 'yes'])
    def test_get_country(self, ex_inp):
        country = get_country()
        self.assertEqual(country, 'Hungary')

    @patch('builtins.input', side_effect = ['15'])
    def test_get_days(self, ex_inp):
        days = get_days()
        self.assertEqual(days, 15)

    @patch('builtins.input', side_effect = ['-1', '10'])
    def test_get_days(self, ex_inp):
        days = get_days()
        self.assertEqual(days, 10)

if __name__ == "__main__":
    unittest.main()


    