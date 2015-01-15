#!/usr/local/bin/pypy

import euler_lib as lib

primes = lib.eratosthenes_sieve(1000)

candidates = [n for n in xrange(1, 150000) if len(lib.prime_factorization(n, primes)) == 4]

i = 0
candidates_len = len(candidates)
while i < candidates_len - 3:
    first = candidates[i + 1] - candidates[i]
    second = candidates[i + 2] - candidates[i + 1]
    third = candidates[i + 3] - candidates[i + 2]

    if first == 1 and second == 1 and third == 1:
        print candidates[i]

    i += 1