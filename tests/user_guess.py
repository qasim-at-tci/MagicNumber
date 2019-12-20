#!/usr/bin/env python
# pylint: disable=W0613,W0622

"""Prompt user for input and return if int.
"""

import unittest

from unittest.mock import patch

def user_guess():
    """Placeholder.
    """
    while True:
        try:
            return int(input('Enter a guess: '))
        except ValueError:
            print('Sorry, try again.')
            raise

class UserGuessTest(unittest.TestCase):
    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='16')
    def test_user_guess_01(self, input):
        """Valid return value.
        """
        self.assertTrue(user_guess(), int)

    @patch('builtins.input', return_value='Derp!')
    def test_user_guess_02(self, input):
        """Invalid return value.
        """
        with self.assertRaises(ValueError):
            user_guess()

if __name__ == '__main__':
    unittest.main()
