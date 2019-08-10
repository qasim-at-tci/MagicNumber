#!/usr/bin/env python
# testing seed value 

import random

for i in range(1):
    random.seed(10)
    for i in range(100):
        print(random.random())
