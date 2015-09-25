#!/usr/local/bin/pypy

from completed.euler_lib import euler_lib

print "hello world"

for num in range(1, 100):
    for den in range(1, 100):
        num_digits = euler_lib.get_digits(num)
        den_digits = euler_lib.get_digits(den)



'''
#!/usr/bin/python

from fractions import Fraction

numerator = range(10, 100)
denominator = range(10, 100)

cross_product = [Fraction(x, y) for x in numerator for y in denominator]

print cross_product
'''
