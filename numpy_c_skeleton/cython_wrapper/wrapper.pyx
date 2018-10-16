# -*- coding: utf-8 -*-

"""
Cython wrapper code around the C library ``sum_array`` function.
"""

# Import numpy
import numpy as np
cimport numpy as np

# Import the definitions from the pxd file
cimport wrapper

# This needs to be run once 
# (https://docs.scipy.org/doc/numpy-1.13.0/reference/c-api.array.html#c.import_array)
np.import_array()

def wrap_sum(
        np.ndarray[np.float64_t, ndim=1, mode='c'] x
        ):
    """
    Wrapper around the sum_array function. Note that the type specification is 
    provided for the input variable.

    """

    cdef long n = x.shape[0]

    # If we want to use "nogil", we have to use "x.data", not "x".
    with nogil:
        total = sum_array(x.data, n)

    return total
