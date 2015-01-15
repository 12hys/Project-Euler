#!/usr/local/bin/pypy

import euler_lib as lib

sieve = lib.eratosthenes_sieve(10000000)
print max(lib.prime_factorization(600851475143, sieve))