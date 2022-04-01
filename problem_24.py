def get_new_permutation(array):
    i, j, k = [len(array)-1] * 3
    while i > 0 and array[i-1] >= array[i]:
        i -= 1
    if i <= 0:
        return None
    while array[j] <= array[i-1]:
        j -= 1
    array[i-1], array[j] = array[j], array[i-1]
    while i < k:
        array[i], array[k] = array[k], array[i]
        i += 1
        k -= 1
    return array

def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 1
    #print(array)
    while True:
        if not array or n == 1000000:
            print(array)
            break
        array = get_new_permutation(array)
        #print(array)
        n += 1
    #print(f"Found {n} permutations")

main()
