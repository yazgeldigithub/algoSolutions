"""
Given two strings a and b, determine if they are isomorphic.

Two strings are isomorphic if the characters in a can be replaced to get b.

All occurrences of a character must be replaced with another character while preserving the order of characters. No
two characters may map to the same character but a character may map to itself.
"""


def csIsomorphicStrings(a, b):
    return len(set(zip(a, b))) == len(set(a)) and len(set(zip(b, a))) == len(set(b))


print(csIsomorphicStrings("odd", "egg"))  # True
print(csIsomorphicStrings("foo", "bar"))  # False
print(csIsomorphicStrings("abca", "zbxz"))  # True
print(csIsomorphicStrings("abc", ""))  # False
