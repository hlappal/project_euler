from my_utils import number_perfectness

def main():
    # Find all numbers below 28124 that cannot be written as a sum of two
    # abundant numbers
    numbers = []
    for n in range(28123, 1, -1):
        if n % 2 == 0:
            if number_perfectness(n / 2) == 1:
                print(f"{n} is the sum of two abundant numbers {n / 2}")
                continue
        numbers.append(n)
    print(sum(numbers))

main()
