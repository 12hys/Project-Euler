import numpy # Run the command `pypy -m pip install git+https://bitbucket.org/pypy/numpy.git`
from problems.euler_lib import euler_lib as lib
from multiprocessing import Pool
from itertools import permutations

def method_one():
    def primes_from_2_to_n(n):
        """ Input n>=6, Returns a array of primes, 2 <= p < n """
        sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
        for i in xrange(1,int(n**0.5)/3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[       k*k/3     ::2*k] = False
                sieve[k*(k-2*(i&1)+4)/3::2*k] = False
        return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

    primes = primes_from_2_to_n(987654322).tolist()
    primes.reverse()

    p = Pool(8)
    pandigital_primes = p.map(lib.is_pandigital_return_number, primes)

    print max(pandigital_primes)

def method_two():
    max_list = []
    string = '987654321'

    while True:
        for p in permutations(string):
            tmp = int(''.join(p))
            if lib.is_pandigital(tmp) and lib.prime(tmp):
                max_list.append(tmp)

        string = string[1:]

        if len(string) < 2:
            break

    print max(max_list)

def method_three():
    number = '7654321'
    max_list = []

    for p in permutations(number):
        tmp = int(''.join(p))
        if lib.is_pandigital(tmp) and lib.prime(tmp):
            max_list.append(tmp)

    print max(max_list)

method_one()
