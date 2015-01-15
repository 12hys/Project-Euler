#!/usr/local/bin/pypy

import collections
import euler_lib as lib

def get_rotations(number):
    rotations = [number]
    d = collections.deque([int(n) for n in str(number)])

    for i in range(len(d) - 1):
        d.rotate(1)
        rotations.append(int(''.join(str(digit) for digit in d)))

    return rotations

answer = 0
sieve = lib.eratosthenes_sieve(1000000)
prime_numbers = filter(lambda x: x < 1000000, sieve)

for n in prime_numbers:
    rotations = get_rotations(n)
    if all(p in prime_numbers for p in rotations):
        answer += 1

print answer
