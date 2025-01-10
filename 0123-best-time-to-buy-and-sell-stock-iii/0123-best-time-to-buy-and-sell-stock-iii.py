class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        buyPrice_idx = 0
        memoizProfits = [[0 for i in range(len(prices))] for i in range(2)] # First price can't make more money
        # first pass
        for i,price in enumerate(prices):
            if price < buyPrice:
                buyPrice_idx = i
                buyPrice = price
            memoizProfits[0][i] = max(price - buyPrice, memoizProfits[0][i-1]) 
        # 2nd pass
        buyPrice = prices[0]
        for i, price in enumerate(prices):
            if i == 0 or i == 1:
                buyPrice = prices[0]
            else:
                updatedPrice = price - memoizProfits[0][i]
                if updatedPrice < buyPrice:
                    buyPrice = price - memoizProfits[0][i]
            memoizProfits[1][i] = max(price - buyPrice, memoizProfits[1][i-1])
        return memoizProfits[1][-1]