class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memoiz = {}
        for i in reversed(range(len(cost))):
            res = cost[i]
            one_step = 0
            two_step = 0
            if i+1 in memoiz:
                one_step = memoiz[i+1]
            if i+2 in memoiz:
                two_step = memoiz[i+2]
            res += min(one_step, two_step)
            memoiz[i] = res 
        print(memoiz)
        def recurse(i):
            if i >= len(cost):
                return 0
            if i in memoiz:
                return memoiz[i]
            else:
                res = cost[i] + min(recurse(i + 1), recurse(i+2))
                memoiz[i] = res
                return res
        return min(memoiz[0], memoiz[1])