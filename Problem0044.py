#!/usr/local/bin/pypy

from math import sqrt
import euler_lib as lib

def generate_pentagonals(ctr, n_range):
    return [n * (3 * n - 1) / 2 for n in n_range]

def generate_hashmap(p_n, jj, kk):
    return [dict(p_k=p_n[k - 1], p_j=p_n[j - 1]) for j in jj for k in kk if lib.is_pentagonal(p_n[j - 1] + p_n[k - 1]) and lib.is_pentagonal(abs(p_n[k - 1] - p_n[j - 1]))]

#sum = p_n[j-1] + p_n[k-1]
#diff = p_n[k-1] - p_n[j-1]

print "Start"
end = 100000
jj = range(1, end + 1)
kk = range(1, end + 1)
p_n = generate_pentagonals(end, range(1, end * 2))
print "Generated Pentagonals"
d = []

hashmap = generate_hashmap(p_n, jj, kk)
print "Generated Hashmap"

for dictionary in hashmap:
    d.append(abs(dictionary['p_k'] - dictionary['p_j']))

print d
