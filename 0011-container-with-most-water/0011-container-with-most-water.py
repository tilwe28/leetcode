class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggest = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r- l) * min(height[l], height[r])
            biggest = max(biggest, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return biggest

    # O(n) time
    # O(1) space