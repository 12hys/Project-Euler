max_steps = 0
start = 0

even = lambda n: (n / 2)
odd = lambda n: (3 * n + 1)


def steps(start):
    step = 1
    while start != 1:
        if start % 2 == 0:
            start = even(start)
        else:
            start = odd(start)
        step += 1

    return step

for i in range(1, 1000000):
    temp_steps = steps(i)

    if temp_steps > max_steps:
        max_steps = temp_steps
        start = i

print str(start)
