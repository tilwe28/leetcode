class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = min(nums[0], nums[-1])
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return res