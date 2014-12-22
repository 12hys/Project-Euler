#!/usr/local/bin/pypy

import cProfile

from multiprocessing import Pool

def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in range(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]

def worker(slide):
    sum_num = sum(sieve[ptr:slide])

    if sum_num % 2 == 0:
        return False

    if sum_num < add_to and is_prime(sum_num):
        return (len(sieve[ptr:slide]), sum_num)

    return False

big_sieve = set(eratosthenes_sieve(10000000))

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

