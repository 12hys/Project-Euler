#!/usr/local/bin/pypy

sum_num = 1
for x in range(3, 1002, 2):
    sum_num += 4*(x**2) - 6*x + 6

print sum_num