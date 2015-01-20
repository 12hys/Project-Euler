#!/usr/local/bin/pypy

x = range(1, 101)
sum_of_squares = 0

for ctr in x:
    sum_of_squares += pow(ctr, 2)

print str(pow(sum(x), 2) - sum_of_squares)
