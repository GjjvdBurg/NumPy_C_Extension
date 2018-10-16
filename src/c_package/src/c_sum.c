/**
 * @file code.c
 * @author G.J.J. van den Burg
 * @date 2017-10-07
 * @brief Implements an array sum function

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

#include "c_sum.h"


/**
 * @brief Sum an array
 *
 * @param[in] 	 array 		array to sum
 * @param[in] 	 n 		length of array
 *
 * @return 			sum of the numbers in the array
 *
 */
double add_array(double *array, long n)
{
	double sum = 0;
	long i;
	for (i=0; i<n; i++)
		sum += array[i];
	return sum;
}
