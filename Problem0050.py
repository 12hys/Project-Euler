#!/usr/local/bin/pypy

import cProfile
import euler_lib as lib

from multiprocessing import Pool

def worker(slide):
    sum_num = sum(sieve[ptr:slide])

    if sum_num % 2 == 0:
        return False

    if sum_num < add_to and is_prime(sum_num):
        return (len(sieve[ptr:slide]), sum_num)

    return False

big_sieve = set(lib.eratosthenes_sieve(10000000))

add_to = 100
sieve = [n for n in big_sieve if n < add_to]

is_prime = lambda x: x in big_sieve

ptr = 0
len_sieve = len(sieve)

pool = Pool(processes=4)

print sieve

while ptr < len_sieve:
    print pool.map(worker, range(len_sieve, ptr, -1))
    ptr = ptr + 1

