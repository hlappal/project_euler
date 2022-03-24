#!/usr/bin/env python3

"""Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


limit = 1000
sum = 0

i = 1
while i * 5 < limit:
    sum += i * 5
    i += 1

i = 1
while i * 3 < limit:
    if i % 5 != 0:
        sum += i * 3
    i += 1

print(sum)
