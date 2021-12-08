import unittest

import numpy as np
import random
from functools import reduce

class RandomTest(unittest.TestCase):
    def test_random_numpy(self):
        mean = 5
        sdev = 3
        sample_size = 1000000

        sample = np.random.normal(mean, sdev, sample_size)

        self.assertAlmostEqual(mean, np.mean(sample), places=2)
        self.assertAlmostEqual(sdev, np.std(sample), places=2)

    #def test_normalvariate(self):
    #    mean = 5
    #    sdev = 3
    #    sample_size = 1000000

    #    sample = random.normalvariate(mean, sdev)

    #    self.assertAlmostEqual(mean, np.mean(sample), places=2)
    #    self.assertAlmostEqual(sdev, np.std(sample), places=2)



    def sum_of_squares(self, l):
        integers = [int(x) for x in l if x[0] != '#']
        squares = [x * x for x in integers]
        return reduce(lambda a, b: a + b, squares)

    def test_sums(self):
        ls = [['1', '2', '3'],
             ['-1', '-2', '-3'],
             ['1', '2', '#100', '3']
            ]
        for l in ls:
            self.assertEqual(self.sum_of_squares(l), 14)
