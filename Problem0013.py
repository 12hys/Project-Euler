'''
Created on Jun 8, 2011

@author: Rhys
'''
file = open('Problem0013.txt', 'r')
x = file.readlines()

sum = 0
for i in x:
    sum += int(i)
print( sum )

file.close()