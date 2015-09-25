sum_num = 0
for x in range(1, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum_num += x

print sum_num
