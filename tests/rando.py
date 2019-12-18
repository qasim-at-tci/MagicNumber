#!/usr/bin/env python

"""Placeholder.
"""

import unittest
from random import Random

def num_gen():
    """Return random number between 1 and 100, inclusive.
    """
    return random.randint(1, 100)

class NumGenTest(unittest.TestCase):
    """Place holder.
    """

    def setUp(self):
        """Placeholder.
        """
        global random
        random = Random(123)

    def test_num_gen(self):
        """Placeholder.
        """
        self.assertEqual(num_gen(), 7)

if __name__ == '__main__':
    unittest.main()
