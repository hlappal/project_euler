import numpy as np
import pandas as pd

TRIANGLE = []

def main():
    # Read data
    with open('problem_18_triangle.csv') as f:
        for row in f.readlines():
            row = list(map(int, row.strip().split(' ')))
            TRIANGLE.append(row)

    n_rows = len(TRIANGLE)
    row_below = np.array(TRIANGLE[-1])
    for i in range(1, n_rows):
        j = n_rows - 1 - i
        row = np.array(TRIANGLE[j])
        sums1 = row + row_below[:-1]
        sums2 = row + row_below[1:]
        row_below = np.max([sums1, sums2], axis=0)
        print(row_below)

main()
