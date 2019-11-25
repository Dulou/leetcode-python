class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minPrice = prices[0]
        res = 0
        
        for price in prices:
            if price - minPrice > res:
                res = price - minPrice
            elif price < minPrice:
                minPrice = price
        return res