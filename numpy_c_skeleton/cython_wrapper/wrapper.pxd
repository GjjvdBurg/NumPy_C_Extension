
cdef extern from "c_package_helper.c":

    double sum_array(char *, long) nogil
