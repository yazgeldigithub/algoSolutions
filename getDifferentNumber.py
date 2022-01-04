def get_different_number(arr):
    seen = {}
    for value in arr:
        if value not in seen:
            seen[value] = True
        # [1, 2, 0 , 5]
    # {1: True, 2: True ...}
    for idx in range(len(arr)):
        if idx not in seen:
            return idx
    return len(arr)


print(get_different_number([1, 2, 0, 5]))
