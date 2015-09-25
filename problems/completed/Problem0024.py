def method_one():
    def get_value(array):
        return int(''.join(str(x) for x in array))

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 1
    digits.sort()
    digits_count = len(digits)
    pivot = digits[0]
    pivot_index = 0
    max_value = get_value(sorted(digits, reverse=True))
    current_permutation = 0

    while current_permutation < max_value and count != 1000000:
        for i in range(digits_count - 1):
            if digits[i] < digits[i + 1]:
                pivot = digits[i]
                pivot_index = i

        ceil = min(filter(lambda x: x > pivot, digits[pivot_index + 1:]))
        ceil_index = digits.index(ceil)

        # swap two array elements
        digits[ceil_index], digits[pivot_index] = digits[pivot_index], digits[ceil_index]

        # sort the sub list after the original pivot index
        digits[pivot_index + 1:] = sorted(digits[pivot_index + 1:])
        current_permutation = get_value(digits)
        count = count + 1

    print current_permutation

def method_two():
    import itertools
    permutes = itertools.permutations([0,1,2,3,4,5,6,7,8,9])

    count = 1
    for p in permutes:
        if count == 1000000:
            print ''.join([str(x) for x in list(p)])
        count += 1

method_two();
