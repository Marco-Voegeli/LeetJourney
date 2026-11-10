class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0]
        for i in range(1, amount + 1):
            new_value = float('inf')
            for coin in coins:
                if i - coin == 0:
                    new_value = min(new_value, 1)
                if i - coin >= 0:
                    new_value = min(new_value, 1 + memo[i - coin])
            memo.append(new_value)
        return memo[-1] if memo[-1] < float('inf') else -1
                    