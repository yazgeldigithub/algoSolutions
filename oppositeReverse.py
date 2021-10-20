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


# Solution 2
def csOppositeReverse(txt):
    word = ""
    for letter in txt:
        if letter != letter.upper():
            word += letter.upper()
        else:
            word += letter.lower()
    return word[:: -1]


# txt = "Hello World"
txt = "ReVeRsE"
print(csOppositeReverse(txt))  # eSrEvEr
