class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for n in nums:
            curr = 1
            if (n-1) not in hashSet:
                while (n + curr) in hashSet:
                    curr += 1
            if curr > longest:
                longest = curr
        return longest
