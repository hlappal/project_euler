from math import floor

def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = floor(n / 10)
    return digits

def init_fac(n, arr):
    digits = get_digits(n)
    for d in digits:
        arr.append(d)
    return arr

def add_term(n, arr):
    carry = 0
    for i,d in enumerate(arr):
        res = d * n + carry
        arr[i] = (res % 10)
        carry = floor(res / 10)
    digits = get_digits(carry)
    for d in digits:
        arr.append(d)
    return arr

def print_array(arr):
    for d in arr:
        print(d, end='')
    print()

def fac(n, arr):
    # print(f"Initializing array...")
    arr = init_fac(n, arr)
    # print_array(arr)
    while n > 1:
        n -= 1
        # print(f"Adding term {n}...")
        add_term(n, arr)
        # print_array(arr)

def main():
    arr = []
    fac(100, arr)
    # print_array(arr)
    print(f"Sum of the digits is {sum(arr)}")

main()
