# Write a function that creates a dictionary with each (key, value) pair being
# the (lower case, upper case) versions of a letter, respectively.
# Examples:
# - mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
# - mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
# - mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

def mapping(letters):
    output = {}
    for letter in letters:
        output[letter] = letter.upper()
    return output


print(mapping(["p", "s"]))  # ➞ { "p": "P", "s": "S" }
print(mapping(["a", "b", "c"]))  # ➞ { "a": "A", "b": "B", "c": "C" }
print(mapping(["a", "v", "y", "z"]))  # ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
