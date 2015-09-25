#!/usr/local/bin/python3
'''
from enum import Enum

Directions = Enum('Directions', 'right down')

class Node:
    def __init__(self, value):
        self.down = None
        self.right = None
        self.value = value

    def insert(self, value, direction):
        if direction == Directions.down:
            self.down = Node(value)
        elif direction == Directions.right:
            self.right = Node(value)

def get_right(mtx, row, col):
    row_length = len(matrix[row])
    rightIdx = col + 1

    if rightIdx < row_length:
        return mtx[row][rightIdx]
    else:
        return None

def get_down(mtx, row, col):
    col_length = len(matrix)
    downIdx = row + 1

    if downIdx < col_length:
        return mtx[downIdx][col]
    else:
        return None
'''

matrix = [
    [131, 673, 234, 123],
    [201, 96, 342, 123],
    [630, 803, 746, 123],
    [630, 803, 746, 123]
]

root = None

for rowIdx in range(len(matrix)):
    row = matrix[rowIdx]
    for colIdx in range(len(row)):
        current_node = None
        value = matrix[rowIdx][colIdx]
        if(rowIdx == 0 and colIdx == 0):
            root = Node(value)
            root.insert(get_right(matrix, 0, 0), Directions.right)
            root.insert(get_down(matrix, 0, 0), Directions.down)


'''
root = Node(131)
root.insert(201, Directions.down)
root.print_tree()
'''
