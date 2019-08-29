#!/usr/bin/env python3
# https://docs.python.org/3/library/ipaddress.html

import ipaddress

address = '159.65.178.169'
print(address)

strip_address = address.split('.',4)
print(strip_address)

octet_8 = ((strip_address[2] + '*' + str(int(strip_address[3]) + 8)).ljust(8, '*')) 
print(octet_8)

octet_12 = ((strip_address[2] + '*' + str(int(strip_address[3]) + 12) + '*' + strip_address[1]).ljust(12, '*')) 
print(octet_12)
