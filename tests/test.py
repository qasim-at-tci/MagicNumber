#!/usr/bin/env python

"""Test suite.
"""

from random import Random

import unittest
from unittest.mock import patch

random = Random()

def num_gen():
    """Generate random integer between 1 and 100, inclusive.
    """
    return random.randint(1, 100)

def user_guess():
    """Prompt user for input.
    Return if int.
    """
    while True:
        try:
            return int(input('Enter a guess: '))
        except ValueError:
            print('Sorry, try again.')

def play_again():
    """Prompt user for input.
    Return input if y/n.
    """
    while True:
        again = input('Play again? Y/N:  ').lower()
        if again in ('y', 'n'):
            return again

def guessing_game():
    """Placeholder.
    """

    magic_number = num_gen()

    for attempt in range(MAX_ATTEMPTS):
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

class NumGenTest(unittest.TestCase):
    """Placeholder.
    """

    def setUp(self):
        """Placholder.
        """
        global random
        random = Random(123)

    def test_num_gen(self):
        """Placeholder.
        """
        self.assertEqual(num_gen(), 7)
        self.assertNotEqual(num_gen(), 49)

class UserGuessTest(unittest.TestCase):
    """Placeholder.
    """

    def get_int(self):
        """Placeholder.
        """
        return input(self)

    @patch('builtins.input', return_value='77')
    def test_user_guess(self, input):
        """Placeholder.
        """
        self.assertTrue(user_guess(), int)

if __name__ == '__main__':
    unittest.main()
