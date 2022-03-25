WORDS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
    80: 'eighty', 90: 'ninety'
}

def to_word(num):
    if num == 1000:
        return 'one thousand'

    ones, tens, hundreds = 0,0,0

    ones = num % 10
    tens = num % 100 - ones
    if tens == 10:
        tens = 0
        ones += 10
    hundreds = num % 1000 - tens - ones

    if hundreds:
        hundreds /= 100
        hundreds = WORDS[hundreds] + ' hundred'
        if tens or ones:
            hundreds += ' and '
    else:
        hundreds = ''

    teens = False
    if tens:
        if tens > 9 and tens < 20:
            teens = True
        tens = WORDS[tens]
    else:
        tens = ''

    if ones:
        if teens:
            ones = ''
        elif tens:
            ones = '-' + WORDS[ones]
        else:
            ones = WORDS[ones]
    else:
        ones = ''

    #print(f"{hundreds }{tens}{ones}")
    return f"{hundreds }{tens}{ones}"

def number_of_letters(word):
    word = word.replace('-','')
    word = word.replace(' ','')
    return len(word)

def main():
    n_total = 0
    for n in range(1, 1001):
        word = to_word(n)
        n_letters = number_of_letters(word)
        n_total += n_letters
        #print(f'"{word}" has {n_letters} letters')
    print(f'{n_total} letters in total')

main()
