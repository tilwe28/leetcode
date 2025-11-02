class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def binarySearch(target):
            l, r = 0, n
            while l < r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            return l
        
        first = binarySearch(target)
        if first == n or nums[first] != target:
            return [-1, -1]
        
        return [first, binarySearch(target + 1) - 1]

"""
initial thoughts:
- just iterate through list and track first and last occurance

O(log n) solution:
binary search to find the starting position
not found when:
    - either the left pointer went all the way to the end,
      occurs when target > max(nums)
    - or left pointer is not at target,
      occurs when target is not in nums but target < max(nums)

otherwise:
- do binary search again but with the target set to target + 1
- doesn't matter if target + 1 is or isn't in nums, but this will find
  the right most position of where target could be
"""