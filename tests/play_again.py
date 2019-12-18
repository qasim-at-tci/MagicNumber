#!/user/bin/python

"""Test to validate user input.
"""

from builtins import input
import unittest

from unittest.mock import patch
from unittest import TestCase

def play_again():
    """Prompt user for input.
    Reprompt if input not y or n.
    """
    while True:
        again = input('Play again? Y/N: ').lower()
        if again in ('y', 'n'):
            return again

class PlayAgainTest(unittest.TestCase):
    """Unit tests.
    """

    def get_input(self):
        return input(self)

    @patch('builtins.input', return_value='y')
    def test_play_again_yes(self, input):
        """Valid return value.
        """
        self.assertEqual(play_again(), 'y')

    @patch('builtins.input', return_value='n')
    def test_play_again_no(self, input):
        """Valid return value.
        """
        self.assertEqual(play_again(), 'n')

if __name__ == '__main__':
    unittest.main()
