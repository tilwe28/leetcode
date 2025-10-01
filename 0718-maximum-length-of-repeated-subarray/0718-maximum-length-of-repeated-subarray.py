class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        res = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
        return res

"""
  3 2 1 4 7
1 0 0 1 0 0
2 0 1 0 0 0
3 1 0 0 0 0
2 0 2 0 0 0
1 0 0 3 0 0

  1 0 1 0 1
0 0 1 0 0 0
1 1 0 2 0 1
1 1 0 1 0 1
1 1 0 1 0 1
1 1 0 1 0 1
"""