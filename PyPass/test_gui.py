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
sg.Popup('IPass: ', TEXT_INPUT)
