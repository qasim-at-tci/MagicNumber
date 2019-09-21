#!/usr/bin/env python3

"""Docstring.
"""

ADDRESS = '159.65.178.169'
print(ADDRESS)

SPLIT_ADDRESS = ADDRESS.split('.', 4)
print(SPLIT_ADDRESS)


def eight_bit_passwd():
    """ Transform IP address to 8-bit password."""
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 8)).ljust(8, '*'))


def twelve_bit_passwd():
    """ Transform IP address to 12-bit password."""
    return((SPLIT_ADDRESS[2] + '*' +
            str(int(SPLIT_ADDRESS[3]) + 12) + '*' + SPLIT_ADDRESS[1]).ljust(12, '*'))

print(eight_bit_passwd(), twelve_bit_passwd())
