'''
Created on Jun 5, 2011

@author: Rhys
'''

print( str(pow(2,1000)) )

sum = 0
for i in str(pow(2,1000)):
    sum += int(i)
print( str(sum) )