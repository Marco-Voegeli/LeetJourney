class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0} # amount, num_coins
        for i in range(1, amount+1):
            min_num = float('inf')
            for choice in coins:
                if i - choice in memo:
                    min_num = min(min_num, 1+memo[i-choice])
                
            memo[i] = min_num
        
        return memo[amount] if memo[amount] < float('inf') else -1