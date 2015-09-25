import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'euler_lib/triangle-18.txt')

file = open(file_path, 'r')
triangle = file.readlines()
file.close()

sum_triangle = []

for i, value in enumerate(triangle):
    triangle[i] = map(int, value.strip().split(' '))

    if i == 0:
        sum_triangle = triangle[i]
        continue

    previous_row = triangle[i - 1]
    for j, previous_value in enumerate(previous_row):



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
