#!/usr/bin/env python3

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""


def main():
    """Main function."""

    count = 0
    n = 2
    while count < 10001:
        if is_prime(n):
            count += 1
            print(f"{n} is the {count}'th prime")
        n += 1

    print("")


def is_prime(n):
    """Check if number n is prime."""

    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

    return prime


if __name__ == '__main__':
    main()
