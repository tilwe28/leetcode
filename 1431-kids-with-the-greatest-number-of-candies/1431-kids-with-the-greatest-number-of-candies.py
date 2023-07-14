class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = [False] * len(candies)
        for i,n in enumerate(candies):
            if n + extraCandies >= max(candies):
                greatest[i] = True
        return greatest