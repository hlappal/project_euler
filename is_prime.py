#!/usr/bin/env python3

from math import sqrt


def is_prime(n):
    """A helper function to determine if a number is prime or not."""
    res = True

    # Check only numbers larger than 1
    if n < 2:
        res = False
    # Check 2 explicitly
    elif n == 2:
        res = True
    # Check even numbers larger than 2
    elif n > 2 and n % 2 == 0:
        res = False
    # Check odd numbers larger than 2 by iterating from 3 to sqrt(n)
    else:
        for i in range(3, int(sqrt(n))+1, 2):
            if n % i == 0:
                res = False

    return res
