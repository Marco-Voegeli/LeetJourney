class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outer_brackets = set()
        stack_p = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack_p.append(i)
            if c == ')':
                l_b = stack_p.pop()
                if not stack_p:
                    outer_brackets.update([i, l_b])
        res = ""
        for i in range(len(s)):
            if i not in outer_brackets:
                res += s[i]
        return res
        