def get_digits_sum(num):
    return list(str(num))

def main():
    pow = 2

    for i in range(1, 15):
        pow *= 2
        print(pow)

    print(get_digits_sum(pow))

main()
