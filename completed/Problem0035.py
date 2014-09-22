#!/usr/local/bin/pypy

import collections


def eratosthenes_sieve():
    n = 1000000
    print "Loading " + str(n) + " primes "
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in xrange(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]


def get_rotations(number):
    rotations = [number]
    d = collections.deque([int(n) for n in str(number)])

    for i in range(len(d) - 1):
        d.rotate(1)
        rotations.append(int(''.join(str(digit) for digit in d)))

    return rotations


def main():
    answer = 0
    sieve = eratosthenes_sieve()
    prime_numbers = filter(lambda x: x < 1000000, sieve)

    for n in prime_numbers:
        rotations = get_rotations(n)
        if all(p in prime_numbers for p in rotations):
            answer += 1

    print "Answer: %s" % (answer)

main()
