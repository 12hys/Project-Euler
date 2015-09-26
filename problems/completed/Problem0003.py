from problems.euler_lib import euler_lib as lib

sieve = lib.eratosthenes_sieve(10000000)
print max(lib.prime_factorization(600851475143, sieve))

# For reference:
def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)

    for i in xrange(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)

    return [i for i in candidates[2:] if i]

def prime_factorization(n, primes):
    return [prime for prime in primes if n % prime == 0]
