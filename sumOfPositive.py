#  Given an array of integers, return the sum of all the positive integers in the array.
import math


def SumOfPositive(input_arr):
    new_array = []
    for num in input_arr:
        if num > 0:
            new_array.append(num)
        else:
            continue
    return math.fsum(new_array)


print(SumOfPositive([1, 2, 3, -4, 5]))  # 11
