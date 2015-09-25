from problems.euler_lib import euler_lib as lib

running_sum = 0
sum_of_divisors = lambda x: sum(lib.get_divisors(x))

for i in xrange(0, 10000):
    sum_i = sum_of_divisors(i)

    if i != sum_i and sum_of_divisors(sum_i) == i:
        running_sum += i

print running_sum

# For reference:
def get_divisors(num):
    return [n for n in range(1, num) if num % n == 0]
