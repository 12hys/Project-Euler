#!/usr/bin/python

m = range(1, 1001)
found = False

for ctr1 in m:
    for ctr2 in range(ctr1,0,-1):
        a = pow(ctr1,2) - pow(ctr2,2)
        b = 2*ctr1*ctr2
        c = pow(ctr1,2) + pow(ctr2,2)
        if(a+b+c == 1000):
            tempa = a
            tempb = b
            tempc = c

print( "a: " + str(tempa) + " b: " + str(tempb) + " c: " + str(tempc) )
print( "a*b*c: " + str(tempa*tempb*tempc) )