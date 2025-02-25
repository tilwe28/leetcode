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
- calculate prefix sum (dummy 0 value)
- have hashmap from seen psum value to index (dummy 0 value)
- check if needed (psum[i] - k) exists in map
    - update max_dist
- add psum in seen (only if not seen before)
"""