# Palindrome

def palindrome(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False


print(palindrome("abba"))  # True
