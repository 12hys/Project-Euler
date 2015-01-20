#!/usr/local/bin/pypy

num_sum = 0
ctr = 0
temp = 0
found = False


def fib(x):
    if (x == 0):
        return 0
    elif (x == 1):
        return 1

    return (fib(x - 1) + fib(x - 2))

while (found == False):
    temp = fib(ctr)
    if (temp <= 4000000):
        if (temp % 2 == 0):
            num_sum += temp
        ctr += 1
    else:
        found = True

print num_sum
