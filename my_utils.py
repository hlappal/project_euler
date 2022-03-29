#!/usr/bin/env python3

from math import sqrt

def is_prime(n):
    """Determine if a number is prime or not"""
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

def quicksort(array, low, high):
    """Sort array by Quicksort"""
    # Find pivot point
    if low < high:
        p = quicksort_partition(array, low, high)
        # Recursive call on the left of pivot
        quicksort(array, low, p - 1)
        # Recursive call on the right of pivot
        quicksort(array, p + 1, high)

def quicksort_partition(array, low, high):
    """Find partition position for Quicksort"""
    p = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= p:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1