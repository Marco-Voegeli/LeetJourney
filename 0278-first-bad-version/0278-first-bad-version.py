# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        last_bad = -1
        while lo <= hi:
            mid = lo + (hi - lo + 1) // 2
            if isBadVersion(mid):
                last_bad = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return last_bad