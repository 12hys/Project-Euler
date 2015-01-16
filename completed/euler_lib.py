import math
import fractions

increment = lambda n: n + 1

def is_pandigital(number):
    digits = get_digits(number)
    compare = range(1, len(digits) + 1)

    return cmp(sorted(digits), compare) == 0

def is_pentagonal(candidate):
    return ((sqrt(24 * candidate + 1) + 1) / 6) % 2 == 0

def get_digits(number):
    return [int(i) for i in str(number)]

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def multiplicative_order(a, n):
    if fractions.gcd(a, n) > 1:
        return 0
    else:
        order = 1
        mod_exp = a
        while mod_exp != 1 :
            order += 1
            mod_exp = (mod_exp * a) % n

    return order

def is_prime(number, sieve):
    return number in sieve

def is_palindrome(number):
    digits = get_digits(number)
    reversed_digits = list(reversed(digits))

    if digits == reversed_digits:
        return True

    return False

def eratosthenes_sieve(n):
    candidates = list(range(n + 1))
    fin = int( n**0.5 )

    for i in xrange( 2, fin + 1 ):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)

    return [i for i in candidates[2:] if i]

def prime_factorization(n, primes):
    return [prime for prime in primes if n % prime == 0]

def get_divisors(num):
    return [n for n in range(1, num) if num % n == 0]

def divisor_count(n):
    ctr = 0
    potential_divisors = range( 1, n + 1 )

    for i in potential_divisors:
        if(n % i == 0):
            ctr += 1

    if( n > 10000 ):
        print n #half-way mark output

    return ctr

def divisor_count_with_sieve(number, sieve):
    if number == 1:
        return 1

    factorization = []
    factor = [i for i in sieve if number % i == 0]

    for x in factor:
        ctr = 1
        temp = number / x
        while(temp % x == 0):
            ctr += 1
            temp = temp / x
        factorization.append(ctr)

    temp = map(increment, factorization)
    return reduce(lambda x, y: x*y, temp)