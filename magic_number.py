from builtins import input			# for handling user input gracefully in Python 2 & 3

#!/usr/bin/env Python3
# Python 2 & 3

"""
Program generates a random number between 1 and 100, inclusive. User has five attempts to correctly guess the number.
"""

# Import Python module
import random					# for "magic" number generation

# Define variable
MAX_ATTEMPTS = 5				# maximum number of guesses

# Define functions
def num_gen():
	"""
	Return random number between 1 and 100, inclusive.
	"""
	return random.randint(1, 100)

def user_guess():
	"""
	Prompt player for guess.
	Return integer.
	"""
	while True:
		try:
			return int(input('Enter a guess:  '))
		except ValueError:
			print('Sorry, try again.')

def play_again():
        """
        Prompt user for Y/N input.
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
		print('Out of guesses! The magic number was: %s.' % magic_number)

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
	print("\nWelcome to the magic number guessing game!\nSee if you can guess the magic number (1-100) in 5 attempts or less.\n")
	game_play()
