import itertools
import operator
import collections
from problems.euler_lib import euler_lib as lib

quad = lambda n_range, a, b: [n**2 + a*n + b for n in n_range]

a_b = xrange(-999, 1000)
sieve = lib.eratosthenes_sieve(1000000)
store = collections.defaultdict()

for a in a_b:
    for b in a_b:
        for ctr in itertools.count(2, 1):
            n_range = xrange(0, ctr)
            values = quad(n_range, a, b)

            if all(lib.is_prime(i, sieve) for i in values):
                continue
            else:
                store[a, b] = len(n_range) - 1
                break

values = max(store.iteritems(), key=operator.itemgetter(1))[0]

print values[0] * values[1]
