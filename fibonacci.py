# fibonacci

def fibonacci(n):
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = a + b
        a = tmp_var
    return result


print(fibonacci(10))  # [1, 1, 2, 3, 5, 8]


def fibonacci1(n):  # O(n)
    lst = [0, 1]  # O(2)
    for i in range(2, n):  # O(n)
        lst.append(lst[i - 2] + lst[i - 1])  # O(2)

    return lst[n - 1]  # O(1)


print(fibonacci1(10))
