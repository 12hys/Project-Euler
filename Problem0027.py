#!/usr/local/bin/pypy

def eratosthenes_sieve(n):
    print "Loading %s primes" % (n)
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in xrange(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]

a_b = range(1, 5)
sieve = eratosthenes_sieve(1000000)
quad = lambda n, a, b: n**2 + a*n + b
consecutive_primes = dict()

for a in a_b:
    for b in a_b:
        consecutive_primes[a] = {b: []}
        n = 2
        while True:
            candidate = quad(n, a, b)
            if candidate in sieve:
                consecutive_primes[a][b].append(candidate)
            else:
                break

            n += 1
print consecutive_primes