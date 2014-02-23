#!/usr/bin/python

x = range(1,101)
sumOfSquares = 0
for ctr in x:
    sumOfSquares += pow(ctr,2)
print( 'Difference: ' + str(pow(sum(x),2)-sumOfSquares) )