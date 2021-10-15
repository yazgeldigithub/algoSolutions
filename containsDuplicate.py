# Given an integer array nums, return true if any value appears at least twice in the array, and return false if
# every element is distinct.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDuplicate(nums):
    return len(nums) != len(set(nums))


print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
print(containsDuplicate([1, 2, 3, 4]))  # False


def containsDuplicate1(nums):
    counter = set()
    for num in nums:
        if num not in counter:
            counter.add(num)
        else:
            return True
    return False


print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
print(containsDuplicate([1, 2, 3, 4]))  # False
