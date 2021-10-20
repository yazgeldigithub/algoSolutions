#  You are given a non-empty array of integers.
#
# One element appears exactly once, with every other element appearing at least twice, perhaps more.
#
# Write a function that can find and return the element that appears exactly once.

from collections import Counter


def csFindTheSingleNumber(nums):
    frequency = Counter(nums)
    for i in frequency:
        if frequency[i] == 1:
            return i


print(csFindTheSingleNumber([1, 1, 2, 1]))  # 2
print(csFindTheSingleNumber([1, 2, 1, 2, 1, 2, 80]))  # 80

"""
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

Elements are counted from an iterable or initialized from another mapping (or counter):

>>>
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

"""