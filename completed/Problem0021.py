#!/usr/local/bin/pypy

import euler_lib as lib

amicable_numbers = []

for number in range(0, 10000):
    sum_of_divisor = sum(lib.get_divisors(number))

    if number != sum_of_divisor:
        if sum(lib.get_divisors(sum_of_divisor)) == number:
            amicable_numbers.append(number)
            amicable_numbers.append(sum_of_divisor)

print sum(lib.unique(amicable_numbers))
