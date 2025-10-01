class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for n in nums:
            curr = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return curr