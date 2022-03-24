#!/usr/bin/env python3

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def main():
    """Main function."""

    # Starting values
    a = 1
    b = 2
    c = 3
    limit = 1000

    while True:
        # Check if the number form a Pythagorean triplet
        if is_triplet(a, b, c):
            if check_limit(a, b, c, limit) == 0:
                break

        # Increment numbers
        c += 1
        # Check if the product abc is larger than 1000
        if check_limit(a, b, c, limit) == 1:
            b += 1
            c = b + 1
            if check_limit(a, b, c, limit) == 1:
                a += 1
                b = a + 1
                c = b + 1

    print(f"The sum of {a} + {b} + {c} is {a + b + c}.")
    print(f"The product {a} * {b} * {c} is {a * b * c}.")


def check_limit(a, b, c, limit):
    """Check if the sum a + b + c hits the limit."""

    val = a + b + c
    ret = 0

    if val < limit:
        ret = -1
    elif val > limit:
        ret = 1

    return ret


def is_triplet(a, b, c):
    """Check if the number form a Pythagorean triplet."""
    if a*a + b*b == c*c:
        return True
    return False


if __name__ == '__main__':
    main()
