"""" Create a function that concatenates the number 7 to the end of every chord in a list. If a chord already ends
with a 7, do not add another 7.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["G", "F7", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
"""


def csMakeItJazzy(chords):
    for index in range(len(chords)):
        if chords[index].__contains__("7"):
            continue
        elif chords == []:
            return []
        else:
            chords[index] = chords[index] + "7"
    return chords


print(csMakeItJazzy(["Dm", "G", "E", "A"]))  # ["Dm7", "G7", "E7", "A7"]
