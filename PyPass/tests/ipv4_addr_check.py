#!/usr/bin/env python3

"""IPv4 validation using `ipaddress` module.

For reference: https://docs.python.org/3/library/ipaddress.html
"""

import ipaddress
import unittest

from unittest.mock import patch

def ipv4_addr_check():
    """Prompt user for IPv4 address, then validate.

    Args:
        arg1 : input

    Raises:
        ValueError: `Bad Value, try again.`

    Returns:
        class 'ipaddress.IPv4Address' if valid, re-prompt if not.
    """

    while True:
        try:
            return ipaddress.IPv4Address(input('Enter a valid IPv4 address: '))
        except ValueError:
            print('Bad value, try again.')
            raise


class IPv4AddrCheckTest(unittest.TestCase):

    """Unit tests.

    Use `patch()` to mock objects for testing.
    """

    @patch('builtins.input', return_value='192.168.1.1')
    def test_ipv4_addr_check_01(self, input):
        """Valid return value.

        Agrs:
            arg1: self
            arg2: input

        Returns:
            class 'ipaddress.IPv4Address'

        """
        self.assertIsInstance(ipv4_addr_check(), ipaddress.IPv4Address)

    @patch('builtins.input', return_value='10.0.0.1')
    def test_ipv4_addr_check_02(self, input):
        """Valid return value.

        Args:
            arg1: self
            arg2: input

        Returns:
            class 'ipaddress.IPv4Address'

        """
        self.assertIsInstance(ipv4_addr_check(), ipaddress.IPv4Address)

    @patch('builtins.input', return_value='Derp!')
    def test_ipv4_addr_check_03(self, input):
        """Invalid return value.

        Args:
            arg1: self
            arg2: input

        Returns:
            Bad value, try again.

        """
        with self.assertRaises(ValueError):
            ipv4_addr_check()

if __name__ == '__main__':
    unittest.main()
