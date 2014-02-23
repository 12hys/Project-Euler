#!/usr/bin/python

#this is a VERY inefficient solution,
#it takes a long time to compute

#wikipedia
def eratosthenes_sieve(n):
    candidates = list(range(n+1))
    fin = int(n**0.5)
    for i in xrange(2, fin+1):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

numberofprimes = 20000000
print( 'Loading primes...' )
primes = eratosthenes_sieve(numberofprimes)
print( 'Done loading primes...' )

def increment(x):
    return x+1

def numOfDivisors(triangleNumber):
    factor = []		#returns the prime factors of a number
    factorization = []	#returns a factorization of the elements in the factor list above. there exists a bijection between factor and factorization
    for x in primes:
        if(triangleNumber % x == 0):
            factor.append(x)
    for x in factor:
        tempCtr = 1
        temp = triangleNumber / x
        while(temp % x == 0):
            tempCtr += 1
            temp = temp / x
        factorization.append(tempCtr)
    temp = map(increment, factorization)
    return reduce(lambda x, y: x*y, temp)
    
found = False
tnumberctr = 10
while(found == False and tnumberctr < numberofprimes):
    triangleNumber = sum(range(1,tnumberctr+1)) #calculates the triangle number
    numofdivs = numOfDivisors(triangleNumber)   #prime factorization method of returning number of divisors of a triangle number
    if numofdivs > 200:
        print( str(triangleNumber) + ': ' + str(numofdivs) )
    
    if(numofdivs >= 500):
        found = True
    else:
        tnumberctr += 1