#!/usr/bin/pypy

def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in range(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]

add_to = 1000
big_sieve = set(eratosthenes_sieve(10000000))
sieve = [n for n in big_sieve if n < add_to]

print sieve
is_prime = lambda x: x in big_sieve

cumsum = [sieve[0] + sieve[1]]
for i in range(2, len(sieve)):
    summed = cumsum[i-2] + sieve[i]

    if summed >= add_to:
        break

    cumsum.append(summed)

print cumsum