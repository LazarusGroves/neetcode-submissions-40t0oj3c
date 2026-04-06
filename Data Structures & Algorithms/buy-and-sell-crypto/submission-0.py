class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 0
        best = 0
        for i,price in enumerate(prices):
            if i == 0:
                minPrice = price
            else:
                minPrice = min(minPrice, price)
            best = max(best, price - minPrice)

        return best
