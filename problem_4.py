#!/usr/bin/env python3

"""Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    num = list(str(num))
    for i in range(len(num) // 2):
        j = i + 1
        if int(num[i]) - int(num[-j]) != 0:
            return False
    return True

largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if is_palindrome(num):
            print('{} is a palindrome'.format(num))
            if num > largest:
                largest = num

print('\n Largest found palindrome is {}'.format(largest))
