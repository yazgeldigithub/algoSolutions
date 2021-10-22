"""Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such
that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once. """


class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in result:
                result[x].append(i)
            else:
                result[x] = [i]
        return list(result.values())


ob1 = Solution()
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(ob1.groupAnagrams(["apt", "pat", "ear", "tap", "are", "arm"]))  # [['apt', 'pat', 'tap'], ['ear', 'are'], ['arm']]
