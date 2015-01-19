#!/usr/local/bin/pypy

import euler_lib as lib
from itertools import permutations

max_list = []
string = '987654321'

while True:
    for p in permutations(string):
        tmp = int(''.join(p))
        if lib.is_pandigital(tmp) and lib.prime(tmp):
            max_list.append(tmp)

    string = string[1:]

    if len(string) < 2:
        break

print max(max_list)
