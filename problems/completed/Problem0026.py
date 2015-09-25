import fractions
from problems.euler_lib import euler_lib as lib

base = 10
primes = lib.eratosthenes_sieve(1001)
cyclic_numbers = []

for prime in primes:
    if(base % prime != 0):
        mult_order = lib.multiplicative_order(base, prime)
        if mult_order == (prime - 1):
            print prime, 'Cyclic Numbers: ', mult_order
