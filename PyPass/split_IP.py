#!/usr/bin/env python3
# https://docs.python.org/3/library/ipaddress.html

import ipaddress

addr = '159.65.178.169'
print(addr)

octet = addr.split('.',4)
print(octet[2], octet[3], octet[1])

octet_int = list(map(int, octet))

print(octet_int[2], octet_int[3], octet_int[1])

