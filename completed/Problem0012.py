#!/usr/local/bin/pypy

import euler_lib as lib

num_primes = 100000
sieve = lib.eratosthenes_sieve(num_primes)

triangle_numbers = [1]
i = 2
ptr = 0
end = 1000000

while i < end:
    triangle_numbers.append(triangle_numbers[ptr] + i)
    ptr = ptr + 1
    i = i + 1

for i in triangle_numbers:
    if lib.divisor_count(i, sieve) > 500:
        print i
        break