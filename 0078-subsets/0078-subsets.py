class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            with_num = []
            for subset in res:
                new = list(subset)
                new.append(num)
                with_num.append(new)
            for subset in with_num:
                res.append(subset)

        return res        
    
"""
backtracking
"""