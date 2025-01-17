class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memoiz = [cost[0], cost[1]]
        if len(cost) >= 3:
            for i in range(2, len(cost)):
                one_s = memoiz[i-1]
                two_s = memoiz[i-2]
                memoiz.append(cost[i] + min(one_s, two_s))

        return min(memoiz[-1], memoiz[-2])