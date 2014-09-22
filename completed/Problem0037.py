#!/usr/local/bin/pypy

def eratosthenes_sieve(n):
    print "Loading " + str(n) + " primes "
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in xrange(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]

def trunked(number):
    trunked_left = [number]
    trunked_right = [number]

    left_digits = [int(x) for x in str(number)]
    right_digits = [int(x) for x in str(number)]

    length_digits = len(left_digits)

    for i in range(length_digits):
        left_digits.pop()
        right_digits.pop(0)

        if(len(left_digits) > 0):
            trunked_left.append(int(''.join([str(x) for x in left_digits])))

        if(len(right_digits) > 0):
            trunked_right.append(int(''.join([str(x) for x in right_digits])))

    return all(t in sieve for t in trunked_left) and all(t in sieve for t in trunked_right)

ctr = 0
number = 10
sieve = eratosthenes_sieve(1000000)
answer = 0

while ctr != 11:
    if trunked(number):
        ctr += 1
        print "Found %s: %s" % (ctr, number)
        answer += number

    number += 1

print "Sum: %s" % answer