#!/usr/bin/python

import csv

names = []
with open( 'names.txt', 'r' ) as text_file:
    rows = csv.reader(text_file, delimiter=',', quotechar='"')
    for row in rows:
        for name in row:
            names.append(name)

names.sort()

total            = 0
position_in_list = 1

for name in names:
    value = 0
    for character in name:
        value += ord(character) - 64
    value *= position_in_list
    position_in_list += 1
    total += value

print total