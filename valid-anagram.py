def isAnagram(s, t):
    if len(s) != len(t):
        return False
        
    countS, countT = {}, {}
        
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) # Everytime we see a char, we increment the value by 1, if we don't see, default value is 0
        countT[t[i]] = 1 + countT.get(t[i], 0)
            
    for c in countS:
        if countS[c] != countT.get(c, 0): # Check if counts are not the same
            return False
            
    return True
    
    
# built in method solution
# return Counter(s) == Counter(t)
# return sorted(s) == sorted(t)
# Time: O(s + t)
# Space O(s + t)
