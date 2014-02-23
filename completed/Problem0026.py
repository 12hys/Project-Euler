#!/usr/bin/python

import fractions

def eratosthenes_sieve( n ):
    candidates = list( range( n + 1 ) )
    fin = int( n**0.5 )
    for i in xrange( 2, fin + 1 ):
        if candidates[ i ]:
            candidates[ 2*i::i ] = [None] * ( n // i - 1 )
    return [i for i in candidates[2:] if i]

def multiplicative_order( a, n ):
    if fractions.gcd( a, n ) > 1:
        return 0
    else:
        order   = 1
        mod_exp = a
        while mod_exp != 1 :
            order   += 1
            mod_exp  = ( mod_exp * a ) % n
    return order

base           = 10
primes         = eratosthenes_sieve( 1001 )
cyclic_numbers = []

for prime in primes:
    if( base % prime != 0 ):
        mult_order = multiplicative_order( base, prime )
        if( mult_order == prime - 1 ):
            print prime, 'Cyclic Numbers:', mult_order