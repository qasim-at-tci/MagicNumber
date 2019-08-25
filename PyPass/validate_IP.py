#!/usr/bin/env python3
# https://docs.python.org/3/library/ipaddress.html

import ipaddress


def validate_IP():
    """Prompt user for IPv4 address, then validate."""

    while True:
        try:
            return ipaddress.IPv4Address(input('Enter a valid IPv4 address: '))
        except ValueError:
            print('Bad value, try again.')

address = validate_IP()

print("{} is a valid IPv4 address".format(address))

octets = str(ipaddress.IPv4Address(address))

print(octets)

split_octets = octets.split('.',4)
print(split_octets) 

#replace_octets = octets.replace('.','*',4)
#print(replace_octets)
