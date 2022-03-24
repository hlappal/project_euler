#!/usr/bin/env python3

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from is_prime import is_prime


def main():
    """Main function."""

    limit = int(2e6)
    sum = 0
    for n in range(2, limit):
        if is_prime(n):
            sum += n

    print(f"The sum of primes under {limit} is {sum}.")


if __name__ == '__main__':
    main()
