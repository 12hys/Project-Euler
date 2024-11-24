def calculate_pentagon_number(n):
    return int(n * (3 * n - 1) / 2)

dict = {}
for i in range(1, 10_000):
    dict[calculate_pentagon_number(i)] = i

# print(dict)

smallest_d = -1

# key = pentagonal, value = n
for j_key, j_value in dict.items():
    for k_key, k_value in dict.items():
        if j_key == k_key:
            continue

        sum = j_key + k_key
        diff = abs(k_key - j_key)
        if sum in dict and diff in dict:
            if smallest_d == -1:
                smallest_d = diff
                print("First diff:", diff)
            smallest_d = min(diff, smallest_d)
            print("Found a diff:", diff, "min(smallest_d):", smallest_d)