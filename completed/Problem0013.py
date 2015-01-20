#!/usr/local/bin/pypy

file = open('Problem0013.txt', 'r')
x = file.readlines()

print sum([int(i) for i in x])

file.close()
