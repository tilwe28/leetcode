class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


"""
- keep a set of nums
- iterate through nums
- if num - 1 is not in the set, then num is a potential start
    - track sequence
"""