"""Given a string (the input will be in the form of an array of characters), write a function that returns the
reverse of the given string.

Examples:

csReverseString(["l", "a", "m", "b", "d", "a"]) -> ["a", "d", "b", "m", "a", "l"] csReverseString(["I", "'", "m",
" ", "a", "w", "e", "s", "o", "m", "e"]) -> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"] """


def csReverseString(chars):
    return chars[::-1]


print(csReverseString(["y", "a", "z", "i", "k"]))
