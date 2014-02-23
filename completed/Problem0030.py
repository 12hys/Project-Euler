#!/usr/bin/pypy

def get_digits( number ):
    digits = []
    number_string = str( number )
    for ch in number_string:
        digits.append(int(ch))
    return digits

def fifth_power( number ):
    return number**5

start = 2
end = (9**5)*6

answer = []
for i in range( start, end + 1 ):
    digits = get_digits( i )
    sum_of_digits = sum( map( fifth_power, digits ) )
    if( i == sum_of_digits ):
        print i, digits
        answer.append(i)

print 'Answer: ' + str( sum( answer ) )