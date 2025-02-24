class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_s = set()
        res = 0
        for a in s:
            if a in set_s:
                set_s.remove(a)
                res += 2
            else:
                set_s.add(a)
        return res + (len(set_s) > 0)