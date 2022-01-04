# You are given an array of characters arr that consists of sequences of characters separated by space characters.
# Each space-delimited sequence of characters defines a word.
# Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

def reverse_words(arr):
  string = "".join(arr)
  wordList = string.split(" ")
  wordList.reverse()
  string = " ".join(wordList)
  resultList = list(string)
  return resultList


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print(reverse_words(arr))
