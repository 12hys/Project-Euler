#!/usr/bin/python

my_range = xrange(1, 21)

def loop(number):
    divisor_count = len([ctr for ctr in my_range if number % ctr == 0])
    if(divisor_count == 20):
        return True

    return False

x = 1

while(loop(x) == False):
    x += 1

print(str(x))
