from itertools import permutations

def extract_number(first, second, third):
    return int(''.join(str(i) for i in [first, second, third]))

def is_divisible(number):
    number = [int(j) for j in list(number)]

    divisible_by_two = extract_number(number[1], number[2], number[3]) % 2 == 0
    divisible_by_three = extract_number(number[2], number[3], number[4]) % 3 == 0
    divisible_by_five = extract_number(number[3], number[4], number[5]) % 5 == 0
    divisible_by_seven = extract_number(number[4], number[5], number[6]) % 7 == 0
    divisible_by_eleven = extract_number(number[5], number[6], number[7]) % 11 == 0
    divisible_by_thirteen = extract_number(number[6], number[7], number[8]) % 13 == 0
    divisible_by_seventeen = extract_number(number[7], number[8], number[9]) % 17 == 0

    return (divisible_by_two and divisible_by_three and divisible_by_five
            and divisible_by_seven and divisible_by_eleven and
            divisible_by_thirteen and divisible_by_seventeen)

digits = '9876543210'
permutations = permutations(digits)

sum = 0
for permutation in permutations:
    if is_divisible(permutation):
        permute_str = ''.join(permutation)
        sum += int(permute_str)
        print(permute_str)

print("Total:", sum)