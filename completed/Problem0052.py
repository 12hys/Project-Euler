#!/usr/local/bin/pypy

def same_digits(numbers):
    digits_list = [sorted([int(digit) for digit in str(number)]) for number in numbers]
    return digits_list[1:] == digits_list[:-1]

x = 2
while True:
    array = [x, 2*x, 3*x, 4*x, 5*x, 6*x]

    if same_digits(array):
        print x
        break

    x = x + 1