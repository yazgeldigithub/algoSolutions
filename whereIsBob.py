# Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list.
# If Bob is not in the array, return -1.
#
# Examples:
#
# csWhereIsBob(["Jimmy", "Layla", "Bob"])  2
# csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"])  0
# csWhereIsBob(["Jimmy", "Layla", "James"])  -1

def whereIsBob(names):
    for bob in range(len(names)):
        if names[bob] == "Bob":
            return bob
    return -1


print(whereIsBob(["Bob", "John", "Bob1"]))  # 0

def whereIsBob1(names):
    for key, value in enumerate(names):
        if value == "Bob":
            return key
    return -1


print(whereIsBob(["Bob", "John", "Bob1"]))  # 0


def whereIsBob2(names):
    for name in names:
        if name == "Bob":
            return name
    return -1


print(whereIsBob(["Bob", "John", "Bob1"]))  # 0
