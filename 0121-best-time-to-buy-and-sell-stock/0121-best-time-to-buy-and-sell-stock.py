class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_p = prices[0]
        curr_profit = 0
        for price in prices:
            if price < min_p:
                curr_profit = max(curr_profit, max_p-min_p)
                min_p = price
                max_p = price
            if price > max_p:
                max_p = price
        return max(curr_profit, max_p-min_p)
