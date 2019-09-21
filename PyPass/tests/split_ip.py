#!/usr/bin/env python3

"""Docstring.
"""

import unittest


ADDRESS = '159.65.178.169'

SPLIT_ADDRESS = ADDRESS.split('.', 4)


def eight_bit_passwd():
    """ Transform IP address to 8-bit password."""
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 8)).ljust(8, '*'))


def twelve_bit_passwd():
    """ Transform IP address to 12-bit password."""
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 12) + '*' + SPLIT_ADDRESS[1]).ljust(12, '*'))


class SplitIPTest(unittest.TestCase):
    """Unit tests.
    """


 
