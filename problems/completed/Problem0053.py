from math import factorial

nCr = lambda n, r: factorial(n) / factorial(r) / factorial(n - r)
ncr_list = [nCr(n, r) for n in range(1, 101) for r in range(1, n + 1)]
print len([i for i in ncr_list if i > 1000000])
