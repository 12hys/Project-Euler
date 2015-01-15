#!/usr/local/bin/pypy

file = open('Problem0013.txt', 'r')
x = file.readlines()

sum_num = 0

for i in x:
    sum_num += int(i)

print sum_num

file.close()