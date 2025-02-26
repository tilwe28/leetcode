class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        max_len = 0
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len

"""
BRUTE FORCE:
- check all subarrays
Time: O(n^2)
Space: O(n^2)

DP:
- subproblem is if you keep taking off last element from nums
- base case is when length is 0
"""