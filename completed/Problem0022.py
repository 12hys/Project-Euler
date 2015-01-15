#!/usr/local/bin/pypy

import csv

with open( 'names.txt', 'r' ) as text_file:
    rows = csv.reader(text_file, delimiter=',', quotechar='"')
    names = [name for row in rows for name in row]

names.sort()

total = 0
position_in_list = 1

for name in names:
    value = 0
    for character in name:
        value += ord(character) - 64
    value *= position_in_list
    position_in_list += 1
    total += value

print total