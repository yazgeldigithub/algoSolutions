# data structure
storage = [None] * 5


def basic_hash_func(string):
    # take in some string
    # turn the string into bytes
    str_bytes = string.encode()

    # set up a counter or a sum variable
    sum = 0
    # iterate over each byte
    for byte in str_bytes:
        # increment our counter / sum by the value at that byte
        sum += byte

    # pass on the value to the caller (return the sum)
    return sum


def put(key, value):
    hash_number = basic_hash_func(key)
    hash_index = hash_number % len(storage)
    storage[hash_index] = value


def get(key):
    hash_number = basic_hash_func(key)
    hash_index = hash_number % len(storage)
    return storage[hash_index]


print(storage)
put("Dave", 20)
put("Yazgeldi", 26)
put("Santa", 100)
print(storage)

daves_age = get("Dave")
print(daves_age)

yazgeldis_age = get("Yazgeldi")
print(yazgeldis_age)

santas_age = get("Santa")
print(santas_age)



