#!/usr/bin/python

import itertools
import math

def is_prime( number ):
    if( number % 2 == 0 ):
        return False

    ctr = 0
    for i in range( 2, int( math.ceil( math.sqrt( number ) ) ) + 1 ):
        if( number % i == 0 ):
            ctr += 1
    if( ctr >= 1 ):
        return False
    else:
        return True

ctr = 1
end = 10001

for i in itertools.count( start = 3, step = 1 ):
    if( is_prime( i ) ):
        ctr += 1
    if( ctr == end ):
        print '#' + str( ctr ) + ') ' + str( i )
        break