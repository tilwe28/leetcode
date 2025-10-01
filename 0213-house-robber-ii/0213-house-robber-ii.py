class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def h1(start, end):
            prev1, prev2 = 0, 0
            for i in range(start, end):
                curr = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(h1(0, len(nums) - 1), h1(1, len(nums)))