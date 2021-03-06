"""" You are given two strings, str_1 and str_2, where str_2 is generated by randomly shuffling str_1 and then adding
one letter at a random position.

Write a function that returns the letter that was added to str_2.

Examples:

csFindAddedLetter(str_1 = "bcde", str_2 = "bdcef") -> "f"
csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
csFindAddedLetter(str_1 = "bf", str_2 = "bfb") -> "b"
"""


def csFindAddedLetter(str_1, str_2):
    m1 = {}
    for i in str_2:
        if i in m1:
            m1[i] += 1
        else:
            m1[i] = 1

    for i in str_1:
        m1[i] -= 1
    for h1 in m1:
        if m1[h1] == 1:
            return h1


print(csFindAddedLetter("bcde", "bdcef"))  # f
print(csFindAddedLetter("bf", "bfb"))  # b
