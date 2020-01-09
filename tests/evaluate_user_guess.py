#!/usr/bin/env python3

"""Placeholder.
"""

import unittest

from unittest.mock import patch

MAGIC_NUMBER = 21
MAX_ATTEMPTS = 1
GUESS = 50

def evaluate_user_guess():
    """Compare user guess to "magic" number.
    Provide feedback.
    """

    for _i in range(MAX_ATTEMPTS):

        if GUESS < MAGIC_NUMBER:
            print('Higher...')
        elif GUESS > MAGIC_NUMBER:
            print('Lower...')
        else:
            print('That\'s right!')
            break

    if GUESS != MAGIC_NUMBER:
        print('Out of guesses! The magic number was: {}.'.format(MAGIC_NUMBER))
