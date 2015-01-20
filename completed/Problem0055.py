#!/usr/local/bin/pypy

import euler_lib as lib

candidates = range(1, 10000)
lychrel_numbers = len(candidates)

for candidate in candidates:
    iteration_ctr = 0
    temp_candidate = candidate

    while iteration_ctr < 50:
        reverse_candidate = int(str(temp_candidate)[::-1])
        test = temp_candidate + reverse_candidate

        if lib.is_palindrome(test):
            lychrel_numbers -= 1
            break

        iteration_ctr += 1
        temp_candidate = test


print lychrel_numbers
