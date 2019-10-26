#!/usr/bin/env python3

"""SimpleGUI.
"""

import PySimpleGUI as sg

LAYOUT = [[sg.Text('Enter valid IPv4 address: ')],
          [sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

WINDOW = sg.Window('IPass', LAYOUT)

EVENT, VALUES = WINDOW.Read()
WINDOW.Close()

TEXT_INPUT = VALUES[0]

SPLIT_ADDRESS = TEXT_INPUT.split('.', 4)

EIGHT_BIT_PASS = SPLIT_ADDRESS[2] + '*' + str(int(SPLIT_ADDRESS[3]) + 8).ljust(8, '*')

sg.Popup('8-bit: ', EIGHT_BIT_PASS)

# SPLIT_ADDRESS = TEXT_INPUT.split('.', 4)
