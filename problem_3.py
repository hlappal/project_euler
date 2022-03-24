#!/usr/bin/env python3


"""Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def get_next_prime(x):
    while True:
        x += 1
        if is_prime(x):
            return x

value = 600851475143
prime = 3
while True:
    if prime == value:
        print(prime)
        break
    if value % prime == 0:
        print('{} is a prime factor of {}'.format(prime, value))
        value /= prime
        prime = 3
    else:
        prime = get_next_prime(prime)
