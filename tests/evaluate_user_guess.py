#!/usr/bin/env python3
# pylint: disable=w0622

"""Placeholder.
"""

import random
import unittest
from unittest.mock import patch

MAGIC_NUMBER = 83
MAX_ATTEMPTS = 5
GUESS = [1, 58, 71, 77, 86]

def evaluate_user_guess():
    """Compare user guess to "magic" number.
    Provide feedback.
    """
    for _i in range(MAX_ATTEMPTS):
        current_guess = random.choice(GUESS)

        if current_guess < MAGIC_NUMBER:
            return 'Higher...'
        elif current_guess > MAGIC_NUMBER:
            return 'Lower...'
        else:
            return 'That\'s right!'

    if GUESS != MAGIC_NUMBER:
        return 'Out of guesses!'

class EvaluateUserGuess(unittest.TestCase):
    """Unit test.
    """
    @patch('builtins.input', return_value='')
    def test_evaluate_user_guess(self, input):
        """Placeholder
        """
        self.assertEqual(evaluate_user_guess(), "Out of guesses!")

if __name__ == '__main__':
    unittest.main()
