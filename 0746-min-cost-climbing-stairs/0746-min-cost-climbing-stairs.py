class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memoiz = {}
    
        def recurse(i):
            if i >= len(cost):
                return 0
            if i in memoiz:
                return memoiz[i]
            else:
                res = cost[i] + min(recurse(i + 1), recurse(i+2))
                memoiz[i] = res
                return res
        return min(recurse(0), recurse(1))