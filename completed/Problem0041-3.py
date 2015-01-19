#!/usr/local/bin/pypy

import euler_lib as lib
from itertools import permutations

number = '7654321'
max_list = []

for p in permutations(number):
    tmp = int(''.join(p))
    if lib.is_pandigital(tmp) and lib.prime(tmp):
        max_list.append(tmp)

print max(max_list)