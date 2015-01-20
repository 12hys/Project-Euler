#!/usr/local/bin/pypy

print str(sum([pow(x, x) for x in xrange(1, 1001)]))[-10:]
