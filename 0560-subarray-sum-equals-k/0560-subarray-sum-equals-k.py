class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = { 0 : 1 }
        res = 0
        curr_sum = 0
        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            if diff in prefix:
                res += prefix[diff]
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
        return res


"""
initial thoughts:
brute force solution would be to check every subarray and see if it sums to k
O(n^2)

have a prefix sum that is a map of the curr prefix sum to count
"""