#!/usr/bin/env python3
# https://docs.python.org/3/library/ipaddress.html

import ipaddress
import unittest

from unittest.mock import patch
from unittest import TestCase

def ipv4_addr_check():
    """Prompt user for IPv4 address, then validate."""

    while True:
        try:
            return ipaddress.IPv4Address(input('Enter a valid IPv4 address: '))
        except ValueError:
            print('Bad value, try again.')
            raise


class IPV4AddrCheckTest(unittest.TestCase):

    @patch('builtins.input', return_value='192.168.1.1')
    def test_ipv4_addr_check_01(self, input):
        self.assertIsInstance(ipv4_addr_check(), ipaddress.IPv4Address)

    @patch('builtins.input', return_value='10.0.0.1')
    def test_ipv4_addr_check_02(self, input):
        self.assertIsInstance(ipv4_addr_check(), ipaddress.IPv4Address)

    @patch('builtins.input', return_value='Derp!')
    def test_ipv4_addr_check_03(self, input):
        with self.assertRaises(ValueError):
            ipv4_addr_check()

if __name__ == '__main__':
    unittest.main()
