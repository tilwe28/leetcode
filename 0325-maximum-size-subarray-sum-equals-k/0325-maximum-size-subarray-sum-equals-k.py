class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        psum = [0]
        for i, n in enumerate(nums):
            curr_sum += n
            psum.append(curr_sum)

        seen = {}
        seen[0] = 0
        max_dist = 0
        for i in range(1, len(psum)):
            needed = psum[i] - k
            if needed in seen:
                max_dist = max(max_dist, i - seen[needed])
            if psum[i] not in seen:
                seen[psum[i]] = i

        return max_dist

"""
BRUTE FORCE:
- check every subarray
Time: O(n^2)

INITIAL THOUGHTS:
- calculate prefix sum
- have hashmap from psum value to index
- check if psum[i] - k exists in map

k = 3
nums: [1, -1, 5, -2, 3]
psum: [0, 1, 0, 5, 3, 6]
needed: [-2, -3, 2, 0, 3]

k = 1
nums: [-2, -1, 2, 1]
psum: [0, -2, -3, -1, 0]
needed: [-3, -4, -2, -1]

k = 1
nums: [-1, 1]
psum: [0, -1, 0]
needed: [-2, -1]
seen: {0: 0, -1: 1}
"""