class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for n in nums:
            if n in unique_nums:
                return True
            unique_nums.add(n)
        return False