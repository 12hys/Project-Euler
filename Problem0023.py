#!/usr/local/bin/pypy

def get_divisors(num):
    arr = []
    for n in range(1, num):
        if( num % n == 0 ):
            arr.append(n)
    return arr

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

debug = True

if(debug):
    upper_limit = 50 + 1
else:
    upper_limit = 28123 + 1

numbers = range(1, upper_limit)

abundant_numbers = []
for n in numbers:
    divisors = get_divisors(n)
    if(sum(divisors) > n):
        abundant_numbers.append(n)

if(debug):
    print abundant_numbers

sum_possibilities = []

for i in range(0, len(abundant_numbers)):
    current = abundant_numbers[i]
    sub_array = abundant_numbers[i+1:]
    for j in sub_array:
        current_sum = j + current
        sum_possibilities.append(current_sum)

sum_possibilities.sort()
sum_possibilities = unique(sum_possibilities)

if(debug):
    print sum_possibilities

answer = []

for x in range(1, max(sum_possibilities)+1):
    if(x not in sum_possibilities):
        answer.append(x)

if(debug):
    print answer
    
print sum(answer)