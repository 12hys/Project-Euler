def getValue(array):
    return int(''.join(str(x) for x in array))

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 1
digits.sort()
digitsCount = len(digits)
pivot = digits[0]
pivotIndex = 0
maxValue = getValue(sorted(digits, reverse=True))
currentPermutation = 0

while currentPermutation < maxValue and count != 1000000:
    for i in range(digitsCount - 1):
        if digits[i] < digits[i + 1]:
            pivot = digits[i]
            pivotIndex = i

    ceil = min(filter(lambda x: x > pivot, digits[pivotIndex + 1:]))
    ceilIndex = digits.index(ceil)

    # swap two array elements
    digits[ceilIndex], digits[pivotIndex] = digits[
        pivotIndex], digits[ceilIndex]

    # sort the sub list after the original pivot index
    digits[pivotIndex + 1:] = sorted(digits[pivotIndex + 1:])
    currentPermutation = getValue(digits)
    count = count + 1

print currentPermutation
