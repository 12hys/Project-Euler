#!/usr/bin/pypy

from extra import eratosthenes_sieve, prime_factorization

list_of_primes = eratosthenes_sieve()

start = 10
end = 20

for i in range( start, end + 1 ):
    print( str( i ) + ':', prime_factorization( i ) )