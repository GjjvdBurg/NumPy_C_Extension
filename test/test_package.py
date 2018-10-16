# -*- coding: utf-8 -*-

"""
Unit test for skeleton package
"""

import numpy as np
import unittest

from numpy_c_skeleton.core import sum_numpy_vec

class SumVecTestCase(unittest.TestCase):

    def test_sum_vec_1(self):
        x = np.ones((10, ))
        self.assertAlmostEqual(x.sum(), sum_numpy_vec(x))

    def test_sum_vec_2(self):
        x = np.random.random((20, ))
        self.assertAlmostEqual(x.sum(), sum_numpy_vec(x))


if __name__ == '__main__':
    unittest.main()
