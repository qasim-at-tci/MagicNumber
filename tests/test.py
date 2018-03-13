#!/usr/bin/env python

import unittest

from random import Random
from unittest.mock import patch
from unittest import TestCase

random = Random()

def num_gen():
	return random.randint(1, 100)

def user_guess():
	while True:
		try:
			return int(input('Enter a guess: '))
		except ValueError:
			print('Sorry, try again.')

def play_again():
	while True:
			again = input('Play again? Y/N:  ').lower()
			if again == 'y' or again == 'n':
					return again

def guessing_game():

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

class num_gen_Test(unittest.TestCase):

	def setUp(self):
		global random
		random = Random(123)

	def test_num_gen(self):
		self.assertEqual(num_gen(), 7)
		self.assertNotEqual(num_gen(), 49)

class user_guess_Test(unittest.TestCase):

	def get_int(self):
		return input(self)

	@patch('builtins.input', return_value='77')
	def test_user_guess(self, input):
		self.assertTrue(user_guess(), int)
"""
class play_again_Test(unittest.TestCase):

	def get_input(self):
		return input(self)

	@patch('builtins.input', return_value='y')
	def test_play_again_yes(self, input):
		self.assertEqual(play_again(), 'y')

	@patch('builtins.input', return_value='n')
	def test_play_again_no(self, input):
		self.assertEqual(play_again(), 'n')

class guessing_game_Test(unittest.TestCase):
"""

if __name__ == '__main__':
	unittest.main()
