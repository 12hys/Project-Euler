#!/usr/bin/python

print( str(pow(2,1000)) )

sum = 0
for i in str(pow(2,1000)):
    sum += int(i)
print( str(sum) )