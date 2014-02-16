#!/usr/bin/python

import math

def is_prime( number ):
    if( number % 2 == 0 ):
        return False

    ctr = 0
    for i in range( 2, int( math.ceil( math.sqrt( number ) ) ) + 1 ):
        if( number % i == 0 ):
            ctr += 1
    if( ctr >= 1 ):
        return False
    else:
        return True

#sieve from wikipedia
def eratosthenes_sieve( number ):
    candidates = list(range(number+1))
    fin = int(number**0.5)
    for i in xrange(2, fin+1):
        if candidates[i]:
            candidates[2*i::i] = [None] * (number//i - 1)
 
    return [i for i in candidates[2:] if i]

listOfPrimes = eratosthenes_sieve(3000000)

def prime_factorization( number ):
    primes = []
    for prime_number in listOfPrimes:
        if( prime_number > number ):
            break

        if( number % prime_number == 0 ):
            primes.append(prime_number)

    return primes

start = 10
end = 20

for i in range( start, end + 1 ):
    print( str( i ) + ':', prime_factorization( i ) )