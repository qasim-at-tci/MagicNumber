#!/usr/bin/env python3 
# https://docs.python.org/3/library/ipaddress.html

import ipaddress 
import unittest

from unittest.mock import patch
from unittest import TestCase


def validate_IP(): 
    """Prompt user for IPv4 address, then validate."""

    while True: 
        try: 
            return str(ipaddress.IPv4Address(input('Enter a valid IPv4 address: ')))
        except ValueError: 
            print('Bad value, try again.') 


class validate_IP_Test(unittest.TestCase): 

    def get_input(self): 
        return input(self)

    @patch('builtins.input', return_value='192.168.1.1')
    def test_validate_IP_01(self, input):
        self.assertTrue(validate_IP(), '192.168.1.1')

    @patch('builtins.input', return_value='10.0.0.1')
    def test_validate_IP_02(self, input):
        self.assertTrue(validate_IP(), '10.0.1.1')


if __name__ == '__main__':
    unittest.main()

