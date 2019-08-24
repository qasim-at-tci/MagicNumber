#!/usr/bin/env python3
# https://docs.python.org/3/library/ipaddress.html

import ipaddress

addr = '159.65.178.169'

octet = addr.split('.',4)

print(octet[2], octet[3], octet[1])


