class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = n + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    triplets.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return triplets