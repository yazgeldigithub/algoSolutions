"""
Challenge #1:
Write a function that retrieves the last n elements from a list.
Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []
Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.

- check if n exceeds the length of the list
  - return "invalid" to the caller
- check if n == 0
  return an empty list to the caller

- get a slice from zero minus n to the last item in the list



"""


# l = [1, 2, 3, 4, 5]
# n = 3
# print(l[0 - n: len(l)])

def last(a, n):
    if n > len(a):
        return "invalid"

    if n == 0:
        return []

    return a[0 - n: len(a)]


# tests
print(last([1, 2, 3, 4, 5], 1))  # ➞ [5]
print(last([4, 3, 9, 9, 7, 6], 3))  # ➞ [9, 7, 6]
print(last([1, 2, 3, 4, 5], 7))  # ➞ "invalid"
print(last([1, 2, 3, 4, 5], 0))  # ➞ []