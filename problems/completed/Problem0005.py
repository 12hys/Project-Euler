my_range = xrange(1, 21)
my_range_len = len(my_range)
is_divisible_by_all = lambda number: len([ctr for ctr in my_range if number % ctr == 0]) == my_range_len

answer = 1
while not is_divisible_by_all(answer):
    answer += 1

print(str(answer))
