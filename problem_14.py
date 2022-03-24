#!/usr/bin/env python3

def collatz(n):
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n + 1
    return int(n)

def run(n):
    terms = 1
    while n != 1:
        n = collatz(n)
        terms += 1
    return terms

def main():
    n = 1000000
    max_start = n
    max_terms = 0
    while n > 0:
        terms = run(n)
        #print(f"Starting from {n}, reached 1 in a chain of {terms} terms")
        if terms > max_terms:
            max_terms = terms
            max_start = n
        n -= 1
    print(f"Longest chain: {max_terms} terms, starting from {max_start}")

main()
