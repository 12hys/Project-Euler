'''
Created on Jul 15, 2011

@author: Rhys
'''
import time

t1 = time.time()
sum = 0
for x in range(1,1001):
    sum += pow(x,x)
t2 = time.time()
print( 'Last 10 digits of the series:' + str(sum)[-10:] )
print( 'This method runs in: ' + str(t2-t1), 'seconds!' )