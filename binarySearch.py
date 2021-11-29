import math


def binarySearch(arr, target):
    left = 0
    right = len(arr)
    while right > left:
        indexToCheck = math.floor((left + right) // 2)
        checking = arr[indexToCheck]

        if checking == target:
            return indexToCheck
        elif target > checking:
            left = indexToCheck + 1
        else:
            right = indexToCheck

    return None


searchable = [1, 2, 7, 8, 22, 28, 41, 58, 67, 71, 94]
target1 = 1

print(binarySearch(searchable, target1))
