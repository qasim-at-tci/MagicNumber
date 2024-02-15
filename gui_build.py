import tkinter as tk
from tkinter import messagebox
import random

MAX_ATTEMPTS = 5

class MagicNumberGameGUI:
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
