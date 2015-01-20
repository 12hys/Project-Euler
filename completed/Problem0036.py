#!/usr/local/bin/pypy

import euler_lib as lib

print sum([num for num in xrange(1000000) if lib.is_palindrome(num) and lib.is_palindrome(bin(num)[2:])])
