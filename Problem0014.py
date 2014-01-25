#!/usr/bin/python

maxSteps = 0
startingNumber = 0

def even(n):
    return (n/2)

def odd(n):
    return (3*n + 1)

def steps(start):
    step = 1
    while (start != 1):
        if(start%2 == 0):
            start = even(start)
        else:
            start = odd(start)
        step += 1
    return step

for i in range(1,1000000):
    tempSteps = steps(i)
    if(tempSteps > maxSteps):
        maxSteps = tempSteps
        startingNumber = i
    print( str(i) + ' has ' + str(tempSteps) + ' steps!' )
print( str(startingNumber) + ' takes the max steps at ' + str(maxSteps) )