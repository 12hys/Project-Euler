#!/usr/bin/pypy

import extra

start = 0
end = 150000 #Trial and error
consec_length = 4
list_of_primes = extra.eratosthenes_sieve()

#all of the numbers where the number of 
#digits of the number equal the distinct
#number of primes
prime_length = []

#this computation is the most intensive
for i in range( start, end + 1 ):
    prime_factorization = extra.prime_factorization( i, list_of_primes )

    if( len( prime_factorization ) == consec_length ):
        print "Found:", str(i)
        prime_length.append( i )

consec_numbers = [[]]
length = len( prime_length )
j = 0

for i, value in enumerate( prime_length ):
    next_index = i + 1
    if( next_index >= length ):
        break;
    elif( ( prime_length[next_index] - value ) == 1 ):
        if( value not in consec_numbers[j] ):
            consec_numbers[j].append( value )
        if( prime_length[next_index] not in consec_numbers[j] ):
            consec_numbers[j].append( prime_length[next_index] )
    else:
        if( len( consec_numbers[j] ) != 0 ):
            consec_numbers.append([])
            j = j+1
        continue

for i in consec_numbers:
    if( len(i) == consec_length ):
        print 'Answer:', i
        break
