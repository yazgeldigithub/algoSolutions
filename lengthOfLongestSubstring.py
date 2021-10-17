# Given a string s, find the length of the longest substring without repeating characters.

def lengtOfLonsgetsSubstring(s):
    start = maxLength = 0
    usedChar = {}

    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength


print(lengtOfLonsgetsSubstring("bbbbb"))  # 1
print(lengtOfLonsgetsSubstring("pwwkew"))  # 3
