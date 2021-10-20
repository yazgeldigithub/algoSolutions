# This sorts the set of all the (unique) words in your string by the word's index in the original list of words.

def csRemoveDuplicateWords(input_str):
    words = input_str.split()
    return " ".join(sorted(set(words), key=words.index))


print(csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta"))
# alpha bravo golf delta
