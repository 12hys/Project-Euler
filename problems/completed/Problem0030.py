from problems.euler_lib import euler_lib as lib

fifth_power = lambda x: x ** 5

answer = []
for i in range(2, (9 ** 5) * 6 + 1):
    sum_of_digits = sum(map(fifth_power, lib.get_digits(i)))

    if(i == sum_of_digits):
        answer.append(i)

print str(sum(answer))
