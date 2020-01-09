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

        if guess < magic_number:
            print('Higher...')
        elif guess > magic_number:
            print('Lower...')
        else:
            print('That\'s right!')
            break

    if guess != magic_number:
        print('Out of guesses! The magic number was: {}.'.format(magic_number))
