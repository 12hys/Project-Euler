import os
import sys

file_path = os.path.join(os.path.dirname(__file__), '..', 'euler_lib/triangle-18.txt')

file = open(file_path, 'r')

triangle = file.readlines()
for i, value in enumerate(triangle):
    triangle[i] = map(int, value.strip().split(' '))

file.close()

sum_triangle = []
triangle_size = len(triangle) - 1
for i, current_row in enumerate(triangle):
    if i == triangle_size:
        break

    temp = []
    next_row = triangle[i + 1]
    for j, value in enumerate(current_row):
        if j == 0:
            temp.append(value + next_row[0])
            temp.append(value + next_row[1])
        elif j == 1:
            print current_row
            print next_row
            print temp
            sys.exit(0)
        else:
            temp[j] = max(temp[j], value + next_row[j])
            temp.append(value + next_row[j + 1])
            #comparitor = next_row[j + 1]
            #value_one = value + comparitor
            #value_two = current_row[j + 1] + comparitor
            #temp.append(max(value_one, value_two))
    sum_triangle = temp

print max(sum_triangle)

'''
listOfNumbers = []

for i in range(len(stringsOfNumbers)):
    stringsOfNumbers[i] = str(stringsOfNumbers[i]).rstrip('\n')
    listOfNumbers.append(tuple(str(stringsOfNumbers[i]).split(' ')))

# convert strings of numbers to int
listOfNumbers = [map(int, x) for x in listOfNumbers]

sumOfTriangle = []
for currentRow in range(len(listOfNumbers)):
    if(currentRow == 0):
        sumOfTriangle = listOfNumbers[currentRow]
    else:
        currentRowTemp = listOfNumbers[currentRow]
        for currentColumnIndex in range(len(currentRowTemp)):
            if(currentColumnIndex == 0):  # first number in triangle
                currentRowTemp[currentColumnIndex] = sumOfTriangle[0] + currentRowTemp[currentColumnIndex]
            # last number in the triangle
            elif (currentColumnIndex == len(currentRowTemp) - 1):
                currentRowTemp[currentColumnIndex] = sumOfTriangle[len(sumOfTriangle) - 1] + currentRowTemp[currentColumnIndex]
            else:  # everything in between
                value1 = currentRowTemp[currentColumnIndex] + sumOfTriangle[currentColumnIndex - 1]
                value2 = currentRowTemp[currentColumnIndex] + sumOfTriangle[currentColumnIndex]
                if(value1 > value2):
                    currentRowTemp[currentColumnIndex] = value1
                else:
                    currentRowTemp[currentColumnIndex] = value2
        sumOfTriangle = currentRowTemp

print max(sumOfTriangle)
'''
