#!/usr/bin/pypy

t = lambda n: n*(n+1)/2
p = lambda n: n*(3*n-1)/2
h = lambda n: n*(2*n-1)

end = 100000

p_list = [p(i) for i in range(1, end)]
h_list = [h(i) for i in range(1, end)]

for n in range(286, end):
    ans = t(n)
    if ans in p_list and ans in h_list:
        print ans, (n, p_list.index(ans) + 1, h_list.index(ans) + 1)
        break
