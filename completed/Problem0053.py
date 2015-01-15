#!/usr/bin/pypy

import math

f = math.factorial
nCr = lambda n, r: f(n) / f(r) / f(n-r)

ans = 0
for n in range(1, 101):
	for r in range(1, n+1):
		if nCr(n, r) > 1000000:
			ans = ans + 1

print ans