my_range = xrange(1, 1001)
cross_product = [[x, y] for x in my_range for y in my_range]

for [x, y] in cross_product:
    a = pow(x, 2) - pow(y, 2)
    b = 2 * x * y
    c = pow(x, 2) + pow(y, 2)

    if(a + b + c == 1000):
        product = a * b * c
        if product > 0:
            print str(product)
            break
