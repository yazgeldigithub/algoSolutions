def productExceptSelf(nums):
    res = []

    acc = 1
    for n in nums:
        res.append(acc)
        acc *= n

    acc = 1
    for i in reversed(range(len(nums))):
        res[i] *= acc
        acc *= nums[i]

    return res

    #  O(1) space and O(n) time


def productExceptSelf2(nums):
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


print(productExceptSelf2([1, 2, 3, 4]))
