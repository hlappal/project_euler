#!/usr/bin/env python3

"""Sum square difference

The sum of the squares of the first ten natural numbers is,

  1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

  (1 + 2 + ... + 10)^2 = 55^2 == 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import numpy as np


sum_squares_ten = np.sum(np.array([x**2 for x in range(1, 11)]))
square_sum_ten = np.sum([x for x in range(1, 11)])**2
difference_ten = square_sum_ten - sum_squares_ten
print(difference_ten)

sum_squares_hundred = np.sum(np.array([x**2 for x in range(1,101)]))
square_sum_hundred = np.sum([x for x in range(1, 101)])**2
difference_hundred = square_sum_hundred - sum_squares_hundred
print(difference_hundred)
