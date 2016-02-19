import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'euler_lib/triangle-18.txt')

file = open(file_path, 'r')

triangle = file.readlines()
for i, value in enumerate(triangle):
    triangle[i] = map(int, value.strip().split(' '))

file.close()

sum_triangle = [triangle.pop(0)[0]]
triangle_size = len(triangle) - 1

for row_index, next_row in enumerate(triangle):
    sum_temp = []
    for col_index, value in enumerate(sum_triangle):
        end_index = len(sum_triangle) - 1
        if col_index == 0:
            sum_temp.append(next_row[0] + value)
            sum_temp.append(next_row[1] + value)
        elif col_index == end_index:
            next_row_end_index = len(next_row) - 1
            sum_temp[col_index] = max(sum_temp[col_index], value + next_row[next_row_end_index - 1])
            sum_temp.append(value + next_row[next_row_end_index])
        else:
            sum_temp[col_index] = max(sum_temp[col_index], value + next_row[col_index])
            sum_temp.append(value + next_row[col_index + 1])

    sum_triangle = sum_temp

print max(sum_triangle)