#!/user/bin/python 
import unittest

from unittest.mock import patch 
from unittest import TestCase

def play_again():
    while True:
        again = input('Play again? Y/N:  ').lower()
        if again == 'y' or again == 'n':
            return again

class play_again_Test(unittest.TestCase):

    def get_input(self):
        return input(self)

    @patch('builtins.input', return_value='y')
    def test_play_again_yes(self, input):
        self.assertEqual(play_again(), 'y')

    @patch('builtins.input', return_value='n')
    def test_play_again_no(self, input):
        self.assertEqual(play_again(), 'n')

if __name__ == '__main__':
    unittest.main()
