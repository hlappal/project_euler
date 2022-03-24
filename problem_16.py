def get_sum(num):
    digits = list(str(num))
    sum = 0
    for d in digits:
        sum += int(d)
    return sum

def main():
    pow = 2

    for i in range(1, 1000):
        pow *= 2

    print(get_sum(pow))

main()
