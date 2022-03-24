#!/usr/bin/env python3

"""Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import numpy as np


primes = np.array([2, 3, 5, 7, 11, 13, 17, 19])
divs = np.arange(1, 21)
num = primes.prod()

while True:
    remainders = []
    for div in divs:
        rem = num % div
        if rem != 0:
            remainders.append(rem)
            for p in primes:
                if rem % p == 0:
                    num *= p
                    break
    if remainders == []:
        break

print('Smallest multiple found: {}'.format(num))
