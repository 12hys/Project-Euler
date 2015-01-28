#!/usr/local/bin/pypy

from multiprocessing import Pool
import cProfile
import euler_lib as lib

<<<<<<< Updated upstream
from multiprocessing import Pool
from operator import itemgetter


def worker(slide):
    sum_num = sum(sieve[ptr:slide])

    if sum_num % 2 != 0 and sum_num < add_to and is_prime(sum_num):
        return (len(sieve[ptr:slide]), sum_num)


big_sieve = set(lib.eratosthenes_sieve(10000000))

add_to = 100000
=======
def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in range(2, fin + 1):
        if candidates[i]:
            candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i]

def main():
    big_sieve = set(eratosthenes_sieve(10000000))

    add_to = 100
    sieve = [n for n in big_sieve if n < add_to]

    print sieve

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
#cProfile.run('main()')

big_sieve = set(eratosthenes_sieve(10000000))

add_to = 100
>>>>>>> Stashed changes
sieve = [n for n in big_sieve if n < add_to]

is_prime = lambda x: x in big_sieve

ptr = 0
<<<<<<< Updated upstream
len_sieve = len(sieve)

print "creating pool..."
pool = Pool(processes=4)

print "creating data..."
data = tuple([[ptr, slide] for ptr in range(len_sieve)
              for slide in range(len_sieve, ptr, -1)])
print "done creating data..."

print "looping..."
results = pool.map(worker, data)
print "looping complete!"

refined = [x for x in results if x != None]

print max(refined, key=itemgetter(0))
=======
len_consec_primes = 0
answer = 0
len_sieve = len(sieve)
pool = Pool(4)

def worker(slide):
    sum_num = sum(sieve[ptr:slide])
    return sum_num
    #if sum_num % 2 != 0 and sum_num < add_to and is_prime(sum_num):
        #print (len(sieve[ptr:slide]), sum_num)
        #temp = len(sieve[ptr:slide])
        #if temp > len_consec_primes:
        #    len_consec_primes = temp
        #    return sum_num

slide = range(len_sieve, 0, -1)
pool.map(worker, slide)
pool.close()
#while ptr < len_sieve:
    #slide = range(len_sieve, ptr, -1)
    #print pool.map(worker, slide)
    #ptr = ptr + 1
>>>>>>> Stashed changes
