class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zero_count1 = sum(1 for n in nums1 if n == 0)
        zero_count2 = sum(1 for n in nums2 if n == 0)

        min_sum1 = sum1 + zero_count1
        min_sum2 = sum2 + zero_count2

        # possible?
        if (zero_count1 == 0 and min_sum2 > sum1) or (zero_count2 == 0 and min_sum1 > sum2):
           return -1
        
        return max(min_sum1, min_sum2)