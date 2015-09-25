import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'euler_lib/triangle-18.txt')

file = open(file_path, 'r')
stringsOfNumbers = file.readlines()
listOfNumbers = []

for i in range(len(stringsOfNumbers)):
    stringsOfNumbers[i] = str(stringsOfNumbers[i]).rstrip('\n')
    '''
    split the strings using the space delim,
    convert to a tuple for conversion to int,
    and append to the main list of numbers
    '''
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
