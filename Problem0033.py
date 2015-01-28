#!/usr/local/bin/pypy

import euler_lib as lib

for num in range(1, 100):
    for den in range(1, 100):
        num_digits = lib.get_digits(num)
        den_digits = lib.get_digits(den)

        
