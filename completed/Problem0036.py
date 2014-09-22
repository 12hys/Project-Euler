#!/usr/local/bin/pypy

def is_palindrome(number):
    digits = [int(i) for i in str(number)]
    reversed_digits = list(reversed(digits))
    if digits == reversed_digits:
        return True

answer = 0
for num in range(1000000):
    if is_palindrome(num) and is_palindrome(bin(num)[2:]):
        answer += num

print answer
