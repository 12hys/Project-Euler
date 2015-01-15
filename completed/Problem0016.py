#!/usr/local/bin/pypy

sum_num = 0
for i in str(pow(2, 1000)):
    sum_num += int(i)

print str(sum_num)