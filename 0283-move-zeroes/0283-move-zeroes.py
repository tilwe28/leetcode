class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, curr = 0, 0
        while i < len(nums) and curr < len(nums):
            if nums[curr] != 0:
                curr += 1
            elif nums[i] != 0 and curr < i:
                nums[curr] = nums[i]
                nums[i] = 0
                i += 1
            else:
                i += 1
            