#!/usr/bin/python

import math

answer = []
for n in range(3, 10000000):
    num = map(lambda x: int(x), str(n)) #array of digits of type int
    sum_of_factorials = sum(map(lambda num: math.factorial(num), num))
    if(sum_of_factorials == n):
        answer.append(sum_of_factorials)

print sum(answer)