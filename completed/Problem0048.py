#!/usr/local/bin/pypy

sum_num = 0
for x in range(1, 1001):
    sum_num += pow(x, x)

print str(sum_num)[-10:]
