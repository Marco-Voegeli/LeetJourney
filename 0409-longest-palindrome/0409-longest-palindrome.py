class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_s = set(s)
        res = 0
        carry = False
        for a in set_s:
            counter = s.count(a, 0)
            if counter % 2 != 0:
                carry = True
            res += 2* (counter//2)
        return res + carry