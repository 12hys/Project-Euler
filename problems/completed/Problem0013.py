import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'euler_lib/problem13.txt')

file = open(file_path, 'r')
x = file.readlines()
file.close()

print str(sum(map(int, x)))[:10]
