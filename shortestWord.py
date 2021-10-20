#  Given a string of words, return the length of the shortest word(s).

def ShortestWord(input_str):
    word = map(len, input_str.split())
    return min(word)


print(ShortestWord(
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"))
# 1
