#!/usr/bin/python

from multiprocessing import Pool
import sys

def number_of_divisors( n ):
    divisor_count      = 0
    potential_divisors = range( 1, n + 1 )

    for i in potential_divisors:
        if( n % i == 0 ):
            divisor_count += 1
    if( n > 10000 ):
        print n #half-way mark output
    return [n, divisor_count]

def unique( seq ):
    seen     = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

if __name__ == '__main__':
    pool    = Pool( 4 ) #Quad-core i5 2500K
    array   = pool.imap( number_of_divisors, range( 1, 100000 + 1 ) )
    pool.close()
    larray  = len( array )
    answers = []

    for i in range( larray + 1 ):
        if( i+1 == larray ):
            print str( len( unique( answers ) ) )
            sys.exit()
        if( array[i][1] == array[i+1][1] ):
            answers.append( array[i][0]   )
            answers.append( array[i+1][0] )