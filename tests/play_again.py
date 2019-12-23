#!/user/bin/env python
# pylint: disable=W0613,W0622

"""Test to validate user input.
"""

import unittest
from unittest.mock import patch

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

    @patch('builtins.input', return_value='y')
    def test_play_again_01(self, input):
        """Valid return value.
        """
        self.assertEqual(play_again(), 'y')

    @patch('builtins.input', return_value='N')
    def test_play_again_02(self, input):
        """Valid return value.
        """
        self.assertEqual(play_again(), 'n')

if __name__ == '__main__':
    unittest.main()
