class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return min(min_val, nums[start])

"""
BINARY SEARCH
~ use start and end pointer
~ check value at middle or nums
~ if middle value is greater than end value, then min value is on right half of list
~ otherwise, min value is on left half of list

~ if on right half, update start pointer to be 1 after mid
~ if on left half, update end pointer to be 1 before mid
"""