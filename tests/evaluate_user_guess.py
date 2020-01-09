#!/usr/bin/env python3

"""Placeholder.
"""

import unitest

from unitest.mock import patch

MAGIC_NUMBER = 50

def evaluate_user_guess():
    """Compare user guess to "magic" number.
    Provide feedback.
    """


    for _i in range(MAX_ATTEMPTS):
        guess = user_guess()

        if guess < MAGIC_NUMBER:
            print('Higher...')
        elif guess > MAGIC_NUMBER:
            print('Lower...')
        else:
            print('That\'s right!')
            break

    if guess != MAGIC_NUMBER:
        print('Out of guesses! The magic number was: {}.'.format(MAGIC_NUMBER))
