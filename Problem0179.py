#!/usr/bin/python

from multiprocessing import Pool
import sys
import euler_lib as lib

pool    = Pool(4)
array   = pool.imap(lib.number_of_divisors, range(1, 100000 + 1))
pool.close()
larray  = len( array )
answers = []

for i in range(larray + 1):
    if(i + 1 == larray):
        print str(len(lib.unique(answers)))
        sys.exit()
    if(array[i][1] == array[i+1][1]):
        answers.append(array[i][0])
        answers.append(array[i+1][0])