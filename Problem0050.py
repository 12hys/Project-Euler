#!/usr/local/bin/pypy

import cProfile
import euler_lib as lib

from multiprocessing import Pool
from operator import itemgetter

def worker(slide):
    sum_num = sum(sieve[ptr:slide])

    if sum_num % 2 != 0 and sum_num < add_to and is_prime(sum_num):
        return (len(sieve[ptr:slide]), sum_num)


big_sieve = set(lib.eratosthenes_sieve(10000000))

add_to = 100000
sieve = [n for n in big_sieve if n < add_to]

is_prime = lambda x: x in big_sieve

ptr = 0
len_sieve = len(sieve)

print "creating pool..."
pool = Pool(processes=4)

print "creating data..."
data = tuple([[ptr, slide] for ptr in range(len_sieve) for slide in range(len_sieve, ptr, -1)])
print "done creating data..."

print "looping..."
results = pool.map(worker, data)
print "looping complete!"

refined = [x for x in results if x != None]

print max(refined, key=itemgetter(0))
