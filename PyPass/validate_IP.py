#!/usr/bin/env python3
# https://docs.python.org/3/library/ipaddress.html

import ipaddress

def validate_IP():
    """Prompt user for IPv4 address, then validate."""

    while True:
        try:
            return str(ipaddress.IPv4Address(input('Enter a valid IPv4 address: ')))
        except ValueError:
            print('Bad value, try again.')

def short_password(): 
    """ Transform IP address to 8-bit password."""
    return((split_address[2] + '*' + str(int(split_address[3]) + 8)).ljust(8, '*')) 

def long_password(): 
    """ Transform IP address to 12-bit password."""
    return((split_address[2] + '*' + str(int(split_address[3]) + 12) + '*' + split_address[1]).ljust(12, '*')) 

if __name__ == '__main__': 
    address = validate_IP()
    split_address = address.split('.',4)
    print(short_password())
    print(long_password())

# print("{} is a valid IPv4 address, continuing...".format(address))
