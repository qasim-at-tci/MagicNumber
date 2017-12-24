import unittest

from unittest.mock import patch
from unittest import TestCase


def get_input(text):
    return input(text)

def play_again():
    while True:
            again = input('Play again? Y/N:  ').lower()
            if again == 'y' or again == 'n':
                    return again

class Test(TestCase):

    @patch('builtins.input', return_value='y')
    def test_play_again_yes(self, input):
        self.assertEqual(play_again(), 'y')

    @patch('builtins.input', return_value='n')
    def test_play_again_no(self, input):
        self.assertEqual(play_again(), 'n')

if __name__ == '__main__':
    unittest.main()
