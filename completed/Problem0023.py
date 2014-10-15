#!/usr/local/bin/pypy

def get_divisors(num):
    return [n for n in range(1, num) if num % n == 0]

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

upper_limit = 28123
numbers = range(1, upper_limit+1)
abundant_numbers = [n for n in numbers if sum(get_divisors(n)) > n]

ctr = range(0, len(abundant_numbers))
sums = unique([abundant_numbers[i] + abundant_numbers[j] for i in ctr for j in ctr])

print sum([n for n in numbers if n not in sums])
