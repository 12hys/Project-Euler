#!/usr/local/bin/pypy


def sum_of_digit_squares(num):
    return sum(map(lambda x: int(x) ** 2, str(num)))

answers = []
for num in range(2, 10000001):
    next_number = sum_of_digit_squares(num)

    while next_number != 89 and next_number != 1:
        next_number = sum_of_digit_squares(next_number)

    if next_number == 89:
        answers.append(num)

print len(answers)
