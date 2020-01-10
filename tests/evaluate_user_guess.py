#!/usr/bin/env python3

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
            print(current_guess)
            print('Higher...')
        elif current_guess > MAGIC_NUMBER:
            print(current_guess)
            print('Lower...')
        else:
            print('That\'s right!')
            break

    if GUESS != MAGIC_NUMBER:
        print('Out of guesses! The magic number was: {}.'.format(MAGIC_NUMBER))

class EvaluateUserGuess(unittest.TestCase):
    """Unit test.
    """
    @patch('builtins.input', return_value='')
    def test_evaluate_user_guess():
        """Placeholder
        """
        self.assetEqual(evaluate_user_guess(), "") 

evaluate_user_guess()
