from random import Random
import unittest

random = Random()

def num_gen():
    return random.randint(1, 100)

class num_gen_Test(unittest.TestCase):

    def setUp(self):
        global random
        random = Random(666)

    def test_num_gen(self):
        self.assertEqual(num_gen(), 59)

if __name__ == '__main__':
    unittest.main()
