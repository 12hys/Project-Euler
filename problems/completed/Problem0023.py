from problems.euler_lib import euler_lib as lib

upper_limit = 28123
numbers = range(1, upper_limit + 1)
abundant_numbers = [n for n in numbers if sum(lib.get_divisors(n)) > n]

ctr = range(0, len(abundant_numbers))
sums = list(set([abundant_numbers[i] + abundant_numbers[j] for i in ctr for j in ctr]))

print sum([n for n in numbers if n not in sums])
