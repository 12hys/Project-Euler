#!/usr/local/bin/pypy

import euler_lib as lib

answer = 0
for num in range(1000000):
    if lib.is_palindrome(num) and lib.is_palindrome(bin(num)[2:]):
        answer += num

print answer
