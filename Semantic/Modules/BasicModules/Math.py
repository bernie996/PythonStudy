'''
    Math Module

If you want to introduce the module, use the next command

import math
from math import pi

sol = math.pi
print(sol)

math.ceil(x)
    Return the ceiling of x, tha smallest integer greater than or equal
    to x. If x is not a float, delegates to x.__ceil__(), which should
    return an Integral value.

math.floor(x)
    Return the floor of x, the largest integer less than or equal to x.
    If x is nor a float, delegates to x.__floor__(), which should return
    an Integral value.

math.comb(n,k)
    Return the number of ways to choose k items from n items without
    repetition and without order.
    Uses the formula:
    n! / (k! * (n-k)!) for k <= n
    0                  for k > n

math.perm(n, k)
    Return the number if ways ti choose k items from n items without
    repetition and with order.
    Uses the formula:
    n! / (n-k)! when k <= n

math.fabs(x)
    Return the absolute value of x.

math.fsum(x)
    Return an accurate floating point sum of values in the iterable.
    Avoids loss of precision by tracking multiple intermediate partial
    sums.

math.pow(x,y)
    Return x raised to the power of y. Converts both its arguments into
    type float.

math.sqrt(x)
    Return the square root of x.

Trigonometrics, results in radians

    math.sin(x)
    math.cos(x)
    math.tan(x)
    math.asin(x)
    math.acos(x)
    math.atan(x)
    math.hypot(*coordinates)
    math.distance(p,q)
        p and q are two points or two sequences of coordinates on the same
        dimension.

Angular
    math.degrees(x)
    math.radians(x)

math.prod(iterable, *, start = 1)
    calculate the product of all elements in the input iterable. The default
    start value of the product is 1.
    When the iterable is empty, return the start value. This function is
    intended specifically for use with numeric values and may reject non-numeric
    types

math.gcd(*integers)
    Return the greatest common divisor of the specified integer arguments.
    If any of the arguments is different to zero, then the reteurned value
    is the largest positive integer that is divisor or all arguments.
    If all arguments are zero, then the returned value is 0.

math.lcm(*integers)
    Return the least common multiple of the specified integer arguments.
    If all arguments are nonzero, then the returned value is the smallest
    positive integer that is a multiple of all arguments. If any of the arguments
    is zero, the the returned value is 0.
    If any of the arguments is zero, the returned value is 0.

math.isclose(a, b, *, rel_tol =, abs_tol = )
    Return true if the values a and b are close to each other al False
    otherwise.
    Whether or not two value are considered close is determined according
    to given absolute and relative tolerances.
    -rel_tol: Is the relative tolerance, meaning that is the maximum allowed
    difference between a and b, relative to the larger absolute value of a or b.
    For example, to set a tolerance of 4%, pass rel_tol = 0.04. The default tolerance
    is 1e-09.
    -abs_tol: Is the minimum absolute tolerance, is usefull for comparisons near zero.
    abs_tol must be at least zero.

math.isnan(x)
    Return True if x is a NaN

Constants
    math.pi == 3.141592...
    math.e == 2.718281...
    math.tau == 6.283185...
    math.inf
        A floating point positive infinity.
    math.nan
        A floating point 'not a number' value.

'''