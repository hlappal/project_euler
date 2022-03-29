#!/usr/bin/env python3

import my_utils

def main():
    with open('names.txt') as f:
        names = f.readlines()
    names = names[0].split(',')
    names = [name.replace('"', '') for name in names]
    my_utils.quicksort(names, 0, len(names) - 1)
    alph_values = [0] * len(names)
    for i,name in enumerate(names):
        alph_values[i] = get_alph_value(name) * (i + 1)
    name_scores = sum(alph_values)
    print(name_scores)

def get_alph_value(name):
    alph_value = 0
    for c in list(name):
        alph_value += ord(c) - 64
    return alph_value

main()