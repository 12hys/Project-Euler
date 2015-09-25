import csv
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'euler_lib/p042_words.txt')

get_num = lambda word: sum(["-ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) for char in word])
tri = lambda n: n * (n + 1) / 2

tri_list = [tri(n) for n in range(1, 100)]

with open(file_path, 'r') as text_file:
    rows = csv.reader(text_file, delimiter=',', quotechar='"')
    words = [word for row in rows for word in row]

print len([word for word in words if get_num(word) in tri_list])
