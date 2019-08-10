#!/usr/bin/env python
# testing seed value 

import random

for i in range(2):
    random.seed(10)
    for i in range(20):
        print(random.random())
