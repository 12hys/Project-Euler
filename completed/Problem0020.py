#!/usr/bin/python

def fact(n):
    if (n == 1): return 1
    else: return n*fact(n-1)
    
x = fact(100)
sum = 0
for i in str(x):
    sum += int(i)
print( str(sum) )