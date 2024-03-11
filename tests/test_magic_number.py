#!/usr/bin/env python3

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from magic_number import submit_guess, check_guess, reset_guess

#import unittest
#from unittest.mock import patch
#import tkinter as tk
#from tkinter import messagebox
#from magic_number import MagicNumberGameGUI

class TestMagicNumberGameGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def test_check_guess_lower(self):
        app = MagicNumberGameGUI(self.root)
        app.magic_number = 50
        app.check_guess(25)
        self.assertEqual(app.status_label.cget("text"), "Higher...")

    def test_check_guess_higher(self):
        app = MagicNumberGameGUI(self.root)
        app.magic_number = 50
        app.check_guess(75)
        self.assertEqual(app.status_label.cget("text"), "Lower...")

    def test_check_guess_correct(self):
        app = MagicNumberGameGUI(self.root)
        app.magic_number = 50
        with patch.object(messagebox, "showinfo") as mock_showinfo:
            app.check_guess(50)
            mock_showinfo.assert_called_once_with("Congratulations!", "You guessed the magic number!")

    def test_check_guess_out_of_guesses(self):
        app = MagicNumberGameGUI(self.root)
        app.magic_number = 50
        app.attempts_remaining = 1
        with patch.object(messagebox, "showinfo") as mock_showinfo:
            app.check_guess(25)
            mock_showinfo.assert_called_once_with("Game Over", "Out of guesses! The magic number was 50.")

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
