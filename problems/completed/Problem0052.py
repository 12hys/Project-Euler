def same_digits(numbers):
    digits_list = [sorted([int(digit) for digit in str(number)]) for number in numbers]
    return all(cmp(x, digits_list[0]) == 0 for x in digits_list)

x = 2
while True:
    array = [x, 2 * x, 3 * x, 4 * x, 5 * x, 6 * x]

    if same_digits(array):
        print x
        break

    x = x + 1
