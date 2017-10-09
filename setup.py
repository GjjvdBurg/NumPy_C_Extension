#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import numpy

from setuptools import setup
from numpy.distutils.misc_util import Configuration

# Set this to True to enable building extensions using Cython. Set it to False·
# to build extensions from the C file (that was previously generated using·
# Cython). Set it to 'auto' to build with Cython if available, otherwise from·
# the C file.
USE_CYTHON = 'auto'

# If we are in a release, we always never use Cython directly
IS_RELEASE = os.path.exists('PKG-INFO')
if IS_RELEASE:
    USE_CYTHON = False

# If we do want to use Cython, we double check if it is available
if USE_CYTHON:
    try:
        from Cython.Build import cythonize
    except ImportError:
        if USE_CYTHON == 'auto':
            USE_CYTHON = False
        else:
            raise

def configuration():

    # This is the numpy Configuration class
    config = Configuration('numpy_c_skeleton', '', None)

    # Wrapper code in Cython uses the .pyx extension if we want to USE_CYTHON, 
    # otherwise it ends in .c.
    wrapper_ext = '*.pyx' if USE_CYTHON else '*.c'

    # Sources include the C/Cython code from the wrapper and the source code of 
    # the C library
    sources = [
            os.path.join('src', wrapper_ext),
            os.path.join('src', 'c_package', 'src', '*.c'),
            ]

    # Dependencies are the header files of the C library and any potential 
    # helper code between the library and the Cython code
    depends = [
            os.path.join('src', 'c_package', 'include', '*.h'),
            os.path.join('src', 'c_package', 'c_package_helper.c')
            ]

    # Register the extension
    config.add_extension('cython_wrapper',
            sources=sources,
            include_dirs=[
                os.path.join('src', 'c_package'),
                os.path.join('src', 'c_package', 'include'),
                numpy.get_include(),
                ],
            depends=depends)

    # Cythonize if necessary
    if USE_CYTHON:
        config.ext_modules = cythonize(config.ext_modules)

    return config


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if __name__ == '__main__':

    # Pull the version from the package __init__.py
    version = re.search("__version__ = '([^']+)'", 
            open('numpy_c_skeleton/__init__.py').read()).group(1)

    # load the configuration
    attr = configuration().todict()

    # Add the other setup attributes
    attr['description'] = 'Python package skeleton for numpy C extension'
    attr['long_description'] = read('README.rst')
    attr['packages'] = ['numpy_c_skeleton']
    attr['version'] = version
    attr['author'] = "G.J.J. van den Burg"
    attr['author_email'] = "gertjanvandenburg@gmail.com"
    attr['license'] = 'GPL v2'
    attr['install_requires'] = ['numpy']
    attr['zip_safe'] = True

    # Finally, run the setup command
    setup(**attr)
