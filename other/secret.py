#!/usr/bin/python

'''
Problem:
You are given a function 'secret()' that accepts a single integer
parameter and returns an integer.  In your favorite programming
language, write a command-line program that takes one command-line
argument (a number) and determines if the secret() function is
additive [secret(x+y) = secret(x) + secret(y)], for all combinations
x and y, where x and y are all prime numbers less than the number
passed via the command-line argument. Describe how to run your examples.
'''

import sys
import math

number = int(sys.argv[1])

secret = lambda x: x
is_additive = lambda (x, y): secret(x+y) == secret(x) + secret(y)

# Slowest way to check primality (with a micro-optimization of sqrt)
# A better method would be to use a pre generated sieve
def is_prime(check):
    for i in xrange(2, int(math.sqrt(check)) + 1):
        if check % i == 0:
            return False

    return True

# Get a list of primes
primes = [i for i in xrange(1, number + 1) if is_prime(i)]

# Cartesian product to produce all combinations
combinations = [(x, y) for x in primes for y in primes]

print all(map(is_additive, combinations))
