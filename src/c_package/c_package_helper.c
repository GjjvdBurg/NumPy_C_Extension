/**
 * @file c_package_helper.c
 * @author G.J.J. van den Burg
 * @date 2017-10-07
 * @brief Helper code between Cython and C library

 * Copyright (C) G.J.J. van den Burg

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU General Public License
 as published by the Free Software Foundation; either version 3
 of the License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

 */

#include <stdlib.h>
#include <numpy/arrayobject.h>
#include "include/c_sum.h"


/**
 * @brief Helper function between Cython and C
 *
 * @details
 * This helper function does almost nothing: it converts the pointer received 
 * from Cython to a double pointer, and calls the C library function.
 *
 * @param x
 * @param n
 *
 * @return
 */
double sum_array(char *x, long n)
{
	double *xd = (double *) x;

	return add_array(xd, n);
}
