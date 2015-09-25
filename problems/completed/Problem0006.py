my_range = xrange(1, 101)

sum_of_squares = sum(map(lambda x: pow(x, 2), my_range))

print str(pow(sum(my_range), 2) - sum_of_squares)
