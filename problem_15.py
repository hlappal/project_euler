import numpy as np

def rec(a):
    if str(a) in d:
        return d[str(a)]
    # End of recursion
    if len(a) == 1:
        return 1
    # If square matrix, split and run recursion on one side
    if a.sum() == 0:
        value = 2*rec(a[1:])
        d[str(a)] = value
        return value
    # If only one path remains
    if (a == -1).all():
        return 1
    # Otherwise go one step forward and perform recursion on both sides
    value = rec(a[:-1]) + rec(a[1:])
    d[str(a)] = value
    return value

def init_a(size):
    a = np.ones((2*size)).astype(int)
    a[size:] = -1
    return a

d = {}
a = init_a(20)
print(rec(a))