#!/usr/bin/python

file = open('Problem0013.txt', 'r')
x = file.readlines()

sum = 0
for i in x:
    sum += int(i)
print( sum )

file.close()