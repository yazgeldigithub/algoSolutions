def my_hash(key):
    sum = 0
    for c in key:
        sum += ord(c)

    return sum


print(my_hash("ABC"))  # 198
