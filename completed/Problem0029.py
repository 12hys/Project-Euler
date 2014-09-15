#!/usr/local/bin/pypy

a = b = range(2, 101)

answer = []
for aa in a:
    for bb in b:
        ans = pow(aa, bb)
        if(ans not in answer):
            answer.append(ans)

print len(answer)
