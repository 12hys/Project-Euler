#!/usr/local/bin/pypy

def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in xrange(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    print "Done loading %s primes" % (n)
    return [i for i in candidates[2:] if i]

sieve = eratosthenes_sieve(1000)
sieve = [n for n in sieve if n < 1000]

is_prime = lambda x: x in sieve

idx = 0
lookahead = idx + 1
answer = 0
sieve_length = len(sieve)
print sieve

while True:
    temp = sum(sieve[idx:lookahead+1])
    if is_prime(temp):
        lookahead += 1

        if lookahead > sieve_length:
            print "Answer: %s" % (temp)
            break
    else:
        idx = lookahead
        lookahead += 1
