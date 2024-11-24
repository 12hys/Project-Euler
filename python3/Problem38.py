import random
import sys


def is_pandigital(digits):
    digits = list([int(i) for i in digits])
    digits.sort()
    return {1, 2, 3, 4, 5, 6, 7, 8, 9} == set(digits)

candidates = range(1, 999999999)
for candidate in candidates:
    multipliers = []
    pandigital = ""
    for n in range(1, 10):
        pandigital += str(candidate * n)
        multipliers.append(n)

        products_length = len(pandigital)
        if products_length > 9:
            break
        elif products_length == 9 and len(multipliers) > 1:
            if is_pandigital(pandigital):
                print("Found number:", pandigital, candidate, multipliers)
            elif int(pandigital) > 987654321:
                sys.exit()
            multipliers.clear()
    if random.randint(1, 1000000) == 1:
        print("On number:", candidate)
