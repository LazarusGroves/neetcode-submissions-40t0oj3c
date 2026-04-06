class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        best = 0
        for price in prices:
            minPrice = min(minPrice, price)
            best = max(best, price - minPrice)

        return best
