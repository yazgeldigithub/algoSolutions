import math


# Factorial using recursion

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 120


# Factorial using math.factorial

def factorial1(n):
    if n <= 1:
        return 1
    else:
        return math.factorial(n)


print(factorial1(5))  # 120
