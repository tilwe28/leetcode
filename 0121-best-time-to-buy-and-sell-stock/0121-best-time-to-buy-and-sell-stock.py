class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for n in prices:
            lowest = min(lowest, n)
            profit = max(profit, n-lowest)
        return profit