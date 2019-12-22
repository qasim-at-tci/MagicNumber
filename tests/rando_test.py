#!/usr/bin/env python

"""Placeholder.
"""

import unittest
from random import Random

random = Random()

def num_gen():
    """Return random integer between 1 and 100, inclusive.
    """
    return random.randint(1, 100)

class NumGenTest(unittest.TestCase):
    """Placeholder.
    """

    def set_up(self):
        """Seed value.
        """
        global random 
        RANDOM = Random(123)

    def test_num_gen(self):
        """Placeholder.
        """
        self.assertEqual(num_gen(), 7)
        self.assertNotEqual(num_gen(), 49)

if __name__ == '__main__':
    unittest.main()
