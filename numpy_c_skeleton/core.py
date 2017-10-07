# -*- coding: utf-8 -*-

"""
Core Python code that works with the Cython wrapper around the C library.

"""

from . import cython_wrapper

def sum_numpy_vec(x):
    """ Compute the sum of a 1-dimensional numpy array """
    return cython_wrapper.wrap_sum(x)
