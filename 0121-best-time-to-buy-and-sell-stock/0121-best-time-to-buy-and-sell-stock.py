class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 2:
            return max(prices[1] - prices[0], 0)
        profit = 0
        lowestPrevPrice = prices[0] # Can't have negative stocks
        for i, price in enumerate(prices[1:]):
            profit = max(price - lowestPrevPrice, profit)
            lowestPrevPrice = min(lowestPrevPrice, price)
        return profit