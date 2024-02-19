#!/usr/bin/env python3

"""No-frills implementation of guess the "magic" number game in Python3.
"""

import tkinter as tk
from tkinter import messagebox
import random

MAX_ATTEMPTS = 5

class MagicNumberGUI:
    """A graphical user interface (GUI) for game.

    Class provides player with a GUI for interacting with the game, incl.:
    window with input field, button, label. Player has five (5) attempts to
    guess the "magic" number (randomly selected number between 1 and 100, inclusive).
    GUI provides feedback as to the player's guess.

    Attributes:
        master (TK): Main window.
        magic_number (int): Randomly generated number player attempts to guess.
        attempts_remaining (int): Number of attempts remaining for player to guess.
        label (Label): Display instructions/feedback to user.
        entry (Entry): Input box for user to enter guess.
        submit_button (Button): Button for user to submit guess.
        status_label (Label): Display feedback/game status.
    """

    def __init__(self, master):
        self.master = master
        self.master.title("Magic Number Game")

        self.magic_number = random.randint(1, 100)
        self.attempts_remaining = MAX_ATTEMPTS

        self.label = tk.Label(master, text="Guess the magic number (1-100):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def submit_guess(self):
        """Retrieve player guess and attempt to convert to integer.
        If input is valid, check guess, else prompt user to retry.
        """

        guess = self.entry.get()
        try:
            guess = int(guess)
            self.check_guess(guess)
        except ValueError:
            messagebox.showerror("Error", "Input must be an integer.")

    def check_guess(self, guess):

        """Evaluate player guess, providing feedback. 
        Track number of attempts.
        Reset game if player can not guess number in number of attempts remaining is 0.
        Clear screen.
        """

        if guess < self.magic_number:
            self.status_label.config(text="Higher...")
        elif guess > self.magic_number:
            self.status_label.config(text="Lower...")
        else:
            messagebox.showinfo("Congratulations!", "You guessed the magic number!")
            self.reset_game()
            return

        self.attempts_remaining -= 1
        if self.attempts_remaining == 0:
            messagebox.showinfo("Game Over",
                f"Out of guesses! "
                f"The magic number was {self.magic_number}.")
            self.reset_game()

        self.entry.delete(0, tk.END)

    def reset_game(self):
        """Set game to defaults.
        """

        self.magic_number = random.randint(1, 100)
        self.attempts_remaining = MAX_ATTEMPTS
        self.status_label.config(text="")
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = MagicNumberGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
