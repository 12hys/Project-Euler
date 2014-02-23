#!/usr/bin/python

fone = 1
ftwo = 1
fthree = fone + ftwo
ctr = 2
while(len(str(fthree)) < 1000):
    fthree = fone + ftwo
    fone = ftwo
    ftwo = fthree
    ctr += 1

print( "ctr: " + str( ctr ) )