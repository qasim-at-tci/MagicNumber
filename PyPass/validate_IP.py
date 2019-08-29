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

print("{} is a valid IPv4 address, continuing...".format(address))

#strip_address = address.split('.',4)
#print(strip_address)

#octet_8 = ((strip_address[2] + '*' + str(int(strip_address[3]) + 8)).ljust(8, '*')) 
#print(octet_8)

#octet_12 = ((strip_address[2] + '*' + str(int(strip_address[3]) + 12) + '*' + strip_address[1]).ljust(12, '*')) 
#print(octet_12)
