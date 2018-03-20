#!/usr/bin/env python

"""
Program generates a random number between 1 and 100, inclusive.
User has five attempts to correctly guess the number.
"""

import random

MAX_ATTEMPTS = 5

def generate_random_number():
	"""
	Return random number between 1 and 100, inclusive.
	"""
	return random.randint(1, 100)

def user_guess():
	"""
	Prompt player, limiting input to integer.
	Return integer.
	"""
	while True:
		try:
			return int(input('Enter a guess:  '))
		except ValueError:
			print('Input must be an integer. Try again.')

def play_again():
    """
    Prompt player, limiting input to "Y" or "N"
	Return y or n.
    """
    while True:
            again = input('Play again? Y/N:  ').lower()
            if again == 'y' or again == 'n':
                    return again

def guessing_game():
	"""
	Compare user guess to magic number.
	Provide user feedback.
	"""
	magic_number = generate_random_number()

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

def game_play():
	"""
	Play game. Allow user to play multiple rounds or resign.
	"""
	while True:
		play = guessing_game()
		another_round = play_again()

		if another_round == 'y':
			continue
		else:
			break

if __name__ == '__main__':
	print("Welcome to the \"Magic\" number guessing game!\nTry to guess the magic number (1-100) in 5 attempts or less.")
	game_play()
