import itertools

def same_digits(numbers):
    digits_list = [sorted([int(digit) for digit in str(number)]) for number in numbers]
    return all(cmp(x, digits_list[0]) == 0 for x in digits_list)

my_array = range(1, 7)

for i in itertools.count(start=1, step=1):
    if same_digits(map(lambda x: x*i, my_array)):
        print i
        break
