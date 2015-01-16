#!/usr/local/bin/pypy

import sys
import euler_lib as lib

products = []

for multiplier in range(1, 10000):
    for multiplicand in range(1, 10000):
        product = multiplier * multiplicand
        number = str(multiplier) + str(multiplicand) + str(product)

        if len(number) == 9 and lib.is_pandigital(int(number)):
            products.append(product)

print sum(lib.unique(products))
