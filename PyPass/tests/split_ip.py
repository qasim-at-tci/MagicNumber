#!/usr/bin/env python3

"""Convert IP address to 8- or 12-bit password.
"""

import unittest

ADDRESS = '192.168.1.1'
SPLIT_ADDRESS = ADDRESS.split('.', 4)


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


class SplitIPTest(unittest.TestCase):
    """Unit tests.
    """

    def test_eight_bit_passwd_01(self):
        """Valid return value.
        """
        self.assertEqual(eight_bit_passwd(), '1*9*****')

    @unittest.expectedFailure
    def test_eight_bit_passwd_02(self):
        """Invalid return value.
        """
        self.assertEqual(eight_bit_passwd(), '1*13*168****')

    def test_twelve_bit_passwd_01(self):
        """Valid return value.
        """
        self.assertEqual(twelve_bit_passwd(), '1*13*168****')

    @unittest.expectedFailure
    def test_twelve_bit_passwd_02(self):
        """Invalid return value.
        """
        self.assertEqual(twelve_bit_passwd(), '1*9*****')

if __name__ == '__main__':
    unittest.main()
