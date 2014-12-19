#!/usr/local/bin/pypy

import cProfile

def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in range(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]

def main():
    big_sieve = set(eratosthenes_sieve(10000000))

    add_to = 10000
    sieve = [n for n in big_sieve if n < add_to]

    is_prime = lambda x: x in big_sieve

    ptr = 0
    len_consec_primes = 0
    answer = 0
    len_sieve = len(sieve)
    
    while ptr < len_sieve:
        slide = range(len_sieve, ptr, -1)
        for i in slide:
            sum_num = sum(sieve[ptr:i])
            if sum_num % 2 != 0 and sum_num < add_to and is_prime(sum_num):
                temp = len(sieve[ptr:i])
                if temp > len_consec_primes:
                    len_consec_primes = temp
                    answer = sum_num
                break

        ptr = ptr + 1

    print(answer)

#main()
cProfile.run('main()')