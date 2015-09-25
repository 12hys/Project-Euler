import math

answer = []
for n in range(3, 10000000):
    sum_of_factorials = sum(map(lambda x: math.factorial(int(x)), str(n)))
    if(sum_of_factorials == n):
        answer.append(sum_of_factorials)

print sum(answer)
