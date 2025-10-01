class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    grid[i][j] = grid[i - 1][j - 1] + 1
                else:
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

"""
  A B C D E
A 1 1 1 1 1
C 1 1 2 2 2
E 1 1 2 2 3

  j b j
b 0 1 1
s 0 1 1
b 0 2 2
"""