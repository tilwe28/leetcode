class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev3, prev2, prev1 = nums[0], nums[1], nums[2] + nums[0]
        for i in range(3, len(nums)):
            curr = max(prev2, prev3) + nums[i]
            prev3 = prev2
            prev2 = prev1
            prev1 = curr
        return max(prev3, prev2, prev1)


"""
keep track of max of last 2
"""