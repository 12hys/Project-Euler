from problems.euler_lib import euler_lib as lib

sieve = lib.eratosthenes_sieve(100000)
triangle_numbers = [1]
i = 2
ptr = 0
end = 1000000

while i < end:
    triangle_numbers.append(triangle_numbers[ptr] + i)
    ptr = ptr + 1
    i = i + 1

for i in triangle_numbers:
    if lib.divisor_count_with_sieve(i, sieve) > 500:
        print i
        break
