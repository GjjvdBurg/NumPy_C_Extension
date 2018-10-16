# -*- coding: utf-8 -*-

"""
Core Python code that works with the Cython wrapper around the C library.

"""

from .cython_wrapper import wrapper

def sum_numpy_vec(x):
    """ Compute the sum of a 1-dimensional numpy array """
    return wrapper.wrap_sum(x)
