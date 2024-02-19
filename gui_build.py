import tkinter as tk
from tkinter import messagebox
import random

MAX_ATTEMPTS = 5

class MagicNumberGUI:
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
        guess = self.entry.get()
        try:
            guess = int(guess)
            self.check_guess(guess)
        except ValueError:
            messagebox.showerror("Error", "Input must be an integer.")

    def check_guess(self, guess):
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
            messagebox.showinfo("Game Over", f"Out of guesses! The magic number was {self.magic_number}.")
            self.reset_game()

        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = MagicNumberGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
