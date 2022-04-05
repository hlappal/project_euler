class Fibonacci:

    def __init__(self):
        self.cache = [[0], [1]]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f"Positive integer number expected, got {n}")

        # Check computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib = add(self(n - 1), self(n - 2))
            #print(f"New fib: {fib}")
            self.cache.append(fib)

        return self.cache[n]


def add(f1, f2):
    # Determine which number is larger and which one is smaller
    if len(f1) >= len(f2):
        l, s = f1.copy(), f2.copy()
    else:
        l, s = f2.copy(), f1.copy()

    # Add the smaller number to the larger one
    for i in range(len(s)):
        l[i] += s[i]

    # Work out the two-digit numbers into one-digit numbers
    m = 0
    for i in range(len(l)):
        l[i] += m
        m = 0
        if l[i] > 9:
            m = int(l[i] / 10)
            l[i] %= 10
        if i == len(l) - 1 and m > 0:
            l.append(m)

    return l


def print_num(n):
    # Print out the array number in right order
    for i in range(len(n)-1, -1, -1):
        print(n[i], end='')
    print()


def main():
    digits = 1000
    fib = Fibonacci()
    i = 0
    while True:
        n = fib(i)
        #print(f"The {i}'th Fibonacci number is {n}")
        if len(n) > digits - 1:
            break
        i += 1
    print(f"The first to have {digits} digits is the {i}'th Fibonacci number:")
    print_num(n)


main()
