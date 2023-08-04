class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target == nums[end]:
                return end

            # case 1 (sorted)
            if nums[mid] > nums[start] and nums[mid] < nums[end]:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # case 2 (min is on left)
            elif nums[mid] < nums[start] and nums[mid] < nums[end]:
                if target > nums[mid] and target < nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1

            # case 3 (min is on right)
            elif nums[mid] > nums[start] and nums[mid] > nums[end]:
                if target < nums[mid] and target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            else:
                break

        return -1 if target != nums[start] else start

"""
BINARY SEARCH
~ use pointers for start and end
~ loop while start < end

checking type of rotation
case 1 (sorted)
    - is sorted if mid is > start and < end
case 2 (min is on left side)
    - occurs if mid < start and < end
case 3 (min is on right side)
    - occurs if mid > start and > end

checking target location based on rotation type
case 1
    - regular binary search
case 2
    - if target > mid and < start, then target is on right side, else target on left
case 3
    - if target < mid and > start, then target is on left side, else target on right

check if mid == target
"""