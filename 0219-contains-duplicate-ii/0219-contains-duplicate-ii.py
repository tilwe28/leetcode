class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1 # slide window down by 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

"""
BRUTE FORCE:
- start l at 0, and check windows of k size starting from l
- if no windows satisfy condition, increment l
- repeat until found or all windows exhausted
Time: O(n * min(n, k))
Space: O(1)

HashMap:
- map number to index in array
- if duplicate is seen, check difference in indices
Time: O(n)
Space: O(n)

HashSet:
- keep set of window size and check duplicates within window
- slide window along updating as needed
Time: O(n)
Space: O(min(n, k))
"""