def singleNumber(nums):
    res = 0
    for i in nums:
        res ^= i
    return res
        
        
        
"""
for i in nums:
            if nums.count(i) == 1:
                return i
                
################################################                
                
hashmap = {}
    for i in nums:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
        
    for key, value in hashmap.items():
        if value == 1:
            return key
"""
