class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)
        copy = list(nums)

        if steps == 0:
            return

        for i in range(len(nums)):
            nums[(i + steps) % len(nums)] = copy[i]