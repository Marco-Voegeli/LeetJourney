class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1 + min(coinchange(12 - 10); coinchange(12 - 6); coinchange(12 - 1)  
        if amount == 0:
            return 0
        memoiz = {0: 0} # Amount : Num of ways
        for coin in coins:
            memoiz[coin] = 1
        for i in range(amount+1):
            if i in memoiz:
                continue
            cost_cases = [i - coin for coin in coins if coin < i]
            cases = [memoiz[case] for case in cost_cases if memoiz[case] > 0]
            if len(cost_cases) == 0 or len(cases) == 0:
                memoiz[i] = 0
                continue                
            memoiz[i] = 1 + min(cases)

        return memoiz[amount] if memoiz[amount] > 0 else -1
