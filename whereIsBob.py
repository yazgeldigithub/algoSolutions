def whereIsBob(names):
    for bob in range(len(names)):
        if names[bob] == "Bob":
            return bob
    return -1


print(whereIsBob(["Bob", "John", "Bob1"]))  # 0
