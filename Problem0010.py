'''
Created on Jun 5, 2011

@author: Rhys
'''

#sieve from wikipedia
def eratosthenes_sieve(n):
    candidates = list(range(n+1))
    fin = int(n**0.5)
    for i in xrange(2, fin+1):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)
 
    return [i for i in candidates[2:] if i]

listOfPrimes = eratosthenes_sieve(2000000)
print( sum(listOfPrimes) )