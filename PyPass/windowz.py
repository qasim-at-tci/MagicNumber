#!/usr/bin/env python3
# pylint: disable=R0901

"""Placeholder.
"""

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import ipaddress

def ipv4_addr_check():
    """Prompt user for IPv4 address, then validate.
    """

    while True:
        try:
            return str(ipaddress.IPv4Address(input('Enter valid IPv4 address: ')))
        except ValueError:
            print('Bad value, try again.')

def eight_bit_passwd():
    """Transform IP address to 8-bit password.
    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 8)).ljust(8, '*'))

def twelve_bit_passwd():
    """Transform IP address to 12-bit password.
    """
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 12) + '*' + SPLIT_ADDRESS[1]).ljust(12, '*'))

class MainWindow(tk.Frame):
    """Class descriptor.
    """

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.config(menu=MenuBar(self))

        self.mode = '8Bit'

        self.label_in = tk.Label(self, text='Enter IP Address:')
        self.label_in.pack()

        self.ip_in = tk.DoubleVar(0)
        text = tk.Entry(self, textvar=self.ip_in)
        text.pack()

        self.ip_out = tk.StringVar(self, '0.0.0.0')
        lbl = tk.Label(self, textvar=self.ip_out)
        lbl.pack()

        btn = tk.Button(self, text='Convert', command=self.convert)
        btn.pack()

        btn = tk.Button(self, text='Quit', command=master.destroy)
        btn.pack()

    def eight_bit_mode(self):
        """Placeholder.
        """
        self.mode = '8-bit'
        self.label_in.config(text='Enter IP address:')

    def twelve_bit_mode(self):
        """Placeholder.
        """
        self.mode = '12-bit'
        self.label_in.config(text='Enter IP address:')

    def convert(self):
        """Placeholder.
        """
        try:
            if self.mode == 'eight_bit_mode':
                ip_out = eight_bit_passwd(self.ip_in.get())
            else:
                ip_out = twelve_bit_passwd(self.ip_in.get())
            self.ip_out.set("{}".format(ip_out))
        except ValueError as err:
            self.ip_out.set("ERROR: {}".format(err))

class MenuBar(tk.Menu):
    """Class descriptor.
    """

    def __init__(self, master):
        tk.Menu.__init__(self, master)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='eight_bit Pass', command=master.eight_bit_mode)
        file_menu.add_command(label='twelve_bit Pass', command=master.twelve_bit_mode)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

def main():
    """Placeholder.
    """
    window = tk.Tk()
    window.title("Py Pass")
    frame = MainWindow(window)
    frame.pack()
    window.mainloop()

if __name__ == '__main__':
    ADDRESS = ipv4_addr_check()
    SPLIT_ADDRESS = ADDRESS.split('.', 4)
    main()
