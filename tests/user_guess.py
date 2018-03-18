#!/usr/bin/env python

import unittest

from unittest.mock import patch 
from unittest import TestCase

def user_guess(): 
    while True: 
        try: 
            return int(input('Enter a guess: '))
        except ValueError: 
            print('Sorry, try again.')

class user_guess_Test(unittest.TestCase): 

    def get_int(self):
        return input(self)

    @patch('builtins.input', return_value='16')
    def test_user_guess(self, input): 
        self.assertTrue(user_guess(), int)
        #self.assertFalse(user_guess(), str)
if __name__ == '__main__':
    unittest.main()
