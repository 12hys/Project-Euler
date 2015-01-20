#!/usr/local/bin/pypy

import euler_lib as lib
from multiprocessing import Pool

p = Pool(8)
divisors = p.map(lib.get_divisor_count, range(2, 10**7))
p.close();

ctr = 0
for n in range(0, len(divisors) - 1):
    if divisors[n] == divisors[n+1]:
        ctr = ctr + 1

print ctr
