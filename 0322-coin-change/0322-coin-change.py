class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def rec(new_amount):
            queue = []
            if new_amount in memo:
                return memo[new_amount]
            if new_amount < 0:
                return math.inf
            if new_amount == 0:
                return 0
            else:
                for c in coins:
                    queue.append(new_amount - c)
                res = 1 + min([rec(a) for a in queue]) 
                memo[new_amount] = res
                return res
        res = rec(amount)
        return res if res < math.inf else -1