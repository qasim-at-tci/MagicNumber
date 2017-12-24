import unittest 

from unittest.mock import patch
from unittest import TestCase


def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class Test(TestCase):

    @patch('builtins.input', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

    @patch('builtins.input', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(answer(), 'you entered no')

if __name__ == '__main__':
    unittest.main()
