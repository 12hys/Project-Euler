'''
Created on Jun 5, 2011

@author: Rhys
'''

input = 600851475143
def isprime(x):
    primeCtr = 0
    for ctr in range(x,0,-1):
        if (x%ctr == 0):
            primeCtr += 1
    if(primeCtr > 2):
        return False
    else:
        return True

start = 2
primeFact = 1
while((start <= input) and (primeFact != input)):
    if(isprime(start)):
        if(input % start == 0):
            print( 'prime factor found: ' + str(start) )
            primeFact = primeFact * start
    start += 1