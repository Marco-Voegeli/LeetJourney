class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #Dyck Path level tracking
        level = 0
        res = ""
        for c in s:
            if c == ')':
                level -= 1
            if level > 0:
                res += c
            if c == '(':
                level += 1
        return res 