#!/usr/bin/env python3

ADDRESS = '159.65.178.169'
print(ADDRESS)

STRIP_ADDRESS = ADDRESS.split('.', 4)
print(STRIP_ADDRESS)

OCTET_8 = ((STRIP_ADDRESS[2] + '*' + str(int(STRIP_ADDRESS[3]) + 8)).ljust(8, '*'))
print(OCTET_8)

OCTET_12 = ((STRIP_ADDRESS[2] + '*' + str(int(STRIP_ADDRESS[3]) + 12) + '*' + STRIP_ADDRESS[1]).ljust(12, '*')) 
print(OCTET_12)
