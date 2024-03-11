#!/usr/bin/env python3

import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import messagebox
from magic_number_game_gui import MagicNumberGameGUI

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

