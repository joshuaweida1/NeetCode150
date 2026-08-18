class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        while prices:
            last = prices.pop()
            if prices:
                profit = max(profit, last - min(prices))
        return profit