class Solution:
    def fib(self, n: int) -> int:
        memoiz = [0, 1]
        for i in range(2, n+1):
            memoiz.append(memoiz[i-1] + memoiz[i-2])
        return memoiz[n]