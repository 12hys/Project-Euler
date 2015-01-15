import math
import fractions

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def multiplicative_order(a, n):
    if fractions.gcd(a, n) > 1:
        return 0
    else:
        order = 1
        mod_exp = a
        while mod_exp != 1 :
            order += 1
            mod_exp = (mod_exp * a) % n

    return order

def is_prime(number, sieve):
    return number in sieve

def is_palindrome(number):
    digits = [int(i) for i in str(number)]
    reversed_digits = list(reversed(digits))

    if digits == reversed_digits:
        return True

    return False

def eratosthenes_sieve():
    n = 10000000
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