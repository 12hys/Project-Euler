import math
import fractions

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def increment(x):
    return x+1

def number_of_digits( num ):
    return len( str( num ) )

'''
def prime_factorization( num, primes ):
    factor = []         #returns the prime factors of a number
    factorization = []  #returns a factorization of the elements in the factor list above. there exists a bijection between factor and factorization
    #temp_primes = [i for i in primes if i <= num]
    for x in primes:
        if( num % x == 0 ):
            factor.append( x )
    for x in factor:
        tempCtr = 1
        temp = num / x
        while( temp % x == 0 ):
            tempCtr += 1
            temp = temp / x
        factorization.append( tempCtr )
    temp = map( increment, factorization )
    return reduce(lambda x, y: x*y, temp)
'''

def multiplicative_order( a, n ):
    if fractions.gcd( a, n ) > 1:
        return 0
    else:
        order = 1
        mod_exp = a
        while mod_exp != 1 :
            order += 1
            mod_exp = (mod_exp * a) % n
    return order

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

def eratosthenes_sieve():
    n = 10000000
    print "Loading " + str( n ) + " primes "
    candidates = list( range( n + 1 ) )
    fin = int( n**0.5 )
    for i in xrange( 2, fin + 1 ):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

def prime_factorization( number, list_of_primes ):
    primes = []
    for prime_number in list_of_primes:
        if( prime_number > number ):
            break

        if( number % prime_number == 0 ):
            primes.append(prime_number)

    return primes