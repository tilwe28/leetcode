class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_counts = defaultdict(int)
        for n in nums:
            mod_counts[n % value] += 1
        
        # greedy search for mex by updating mod_counts
        mex = 0
        while mod_counts[mex % value] > 0:
            # while it's possible a multiple of mex exists, incrememnt mex
            mod_counts[mex % value] -= 1
            mex += 1
        
        # found first value that would be exluded in the continuous array
        return mex

"""
initial thoughts:
- enumerate through nums:
    - set nums[i] = n % value
    - taking the mod of each num gives the minimum positive number that
      can be achieved by adding or subtracting value any number of times
- find max num in modified array
- find the number closest to max thats less than max not in the array
    - can do this in multiple ways
    - one way is have a set from 0 to max_mod - 1
    - then do set subtraction: mex = range_set - set(nums)
    - res = max(mex)

^ above is wrong
- insight is that if we have multiple mod values, then we could
  construct an array with higher multiples, which makes it possible
  to have a continuous array that goes on for an amount > value
- to fix this, get a frequency, and keep searching for the mex
  while updating the frequency
"""