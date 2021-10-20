"""
Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum) of all integers in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
"""


def csAnythingButFive(start, end):
    count = 0
    new_list = []
    for num in range(start, end + 1):
        str_num = str(num)
        if '5' in str_num:
            continue
        count += 1
    return count


print(csAnythingButFive(1, 5))  # 4
print(csAnythingButFive(1, 9))  # 8
print(csAnythingButFive(4, 17))  # 12
print(csAnythingButFive(-4, 17))  # 20
print(csAnythingButFive(0, 7))  # 7
print(csAnythingButFive(-14, -5))  # 9
