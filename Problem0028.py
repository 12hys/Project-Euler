#!/usr/bin/python

#square = 1001*1001
#ctr = 3 #start at the 3x3 grid
#totSum = 1 #we know the first number is 1
#lastNum = 2 #lastNum is always the previous number + 1
#skip = 1 #we only skip one in the 3x3 grid

#while(ctr*ctr <= square):
#    for x in range(1,5):
#        totSum += (lastNum + skip)
#        lastNum = lastNum + skip + 1
#    skip += 2
#    ctr += 2
#print 'Sum:',totSum

sum = 1
for x in range(3, 1002, 2):
    sum += 4*(x**2) - 6*x + 6
print( sum )