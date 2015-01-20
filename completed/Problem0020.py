#!/usr/local/bin/pypy


def fact(n):
    if (n == 1):
        return 1

    return n * fact(n - 1)

x = fact(100)
sum_num = 0
for i in str(x):
    sum_num += int(i)

print str(sum_num)
