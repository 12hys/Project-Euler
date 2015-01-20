#!/usr/local/bin/pypy

import euler_lib as lib

print max([i * j for i in range(100, 1000) for j in range(100, 1000) if lib.is_palindrome(i * j)])
