# Write a function that takes a string as input and returns that string in reverse order, with the opposite casing
# for each character within the string.
#
# Examples:
#
# csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
# csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
# csOppositeReverse("Radar") ➞ "RADAr"

def oppositeReverse(txt):
    return txt.swapcase()[::-1]


print(oppositeReverse("Hello World"))  # DLROw OLLEh
