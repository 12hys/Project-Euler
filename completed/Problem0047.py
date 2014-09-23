#!/usr/local/bin/pypy

def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in xrange(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    print "Done loading %s primes" % (n)
    return [i for i in candidates[2:] if i]


def prime_factorization(number, list_of_primes):
    return [p for p in list_of_primes if number % p == 0]

primes = eratosthenes_sieve(1000)

candidates = [n for n in xrange(1, 150000) if len(prime_factorization(n, primes)) == 4]

i = 0
candidates_len = len(candidates)
while i < candidates_len - 3:
    first = candidates[i + 1] - candidates[i]
    second = candidates[i + 2] - candidates[i + 1]
    third = candidates[i + 3] - candidates[i + 2]

    if first == 1 and second == 1 and third == 1:
        print candidates[i]

    i += 1