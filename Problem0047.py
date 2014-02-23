#!/usr/bin/python

import extra

start = 10
end = 100
list_of_primes = extra.eratosthenes_sieve()

#all of the numbers where the number of 
#digits of the number equal the distinct
#number of primes
prime_length = []

for i in range( start, end + 1 ):
    number_of_digits = extra.number_of_digits( i )
    prime_factorization = extra.prime_factorization( i, list_of_primes )

    if( number_of_digits == len( prime_factorization ) ):
        prime_length.append( i )

print prime_length
