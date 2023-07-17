class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in valueMap:
                return [valueMap[diff], i]
            valueMap[n] = i
        return