#!/usr/bin/env python3

"""Placeholder.
"""

import unitest

from unitest.mock import patch

MAGIC_NUMBER = 21
MAX_ATTEMPTS = 1
GUESS = 50

def evaluate_USER_GUESS():
    """Compare user GUESS to "magic" number.
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
        print('Out of GUESSes! The magic number was: {}.'.format(MAGIC_NUMBER))
