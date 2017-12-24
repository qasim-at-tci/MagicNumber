#!/usr/bin/env python

import unittest

from random import Random
from unittest.mock import patch
from unittest import TestCase

random = Random()

def num_gen():
    return random.randint(1, 100)

def play_again():
    while True:
            again = input('Play again? Y/N:  ').lower()
            if again == 'y' or again == 'n':
                    return again

class num_gen_Test(unittest.TestCase):

    def setUp(self):
        global random
        random = Random(666)

    def test_num_gen(self):
        self.assertEqual(num_gen(), 59)

class play_again_Test(unittest.TestCase):

    def get_input(text):
        return input(text)

    @patch('builtins.input', return_value='y')
    def test_play_again_yes(self, input):
        self.assertEqual(play_again(), 'y')

    @patch('builtins.input', return_value='n')
    def test_play_again_no(self, input):
        self.assertEqual(play_again(), 'n')

if __name__ == '__main__':
    unittest.main()
