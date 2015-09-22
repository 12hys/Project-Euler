#!/usr/bin/python

my_range = xrange(1, 21)
divisor_count = lambda number: len([ctr for ctr in my_range if number % ctr == 0])

answer = 1
while(divisor_count(answer) != 20):
    answer += 1

print(str(answer))
