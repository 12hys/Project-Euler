import cProfile

def method_one():
    numbers = range(2, 101)
    answer = []
    for aa in numbers:
        for bb in numbers:
            ans = pow(aa, bb)
            if(ans not in answer):
                answer.append(ans)

    print "Answer: %s" % (len(answer))


def method_two():
    numbers = range(2, 101)
    answer = len(list(set([pow(a, b) for a in numbers for b in numbers])))
    print "Answer: %s" % (answer)

cProfile.run('method_one()')
cProfile.run('method_two()')
