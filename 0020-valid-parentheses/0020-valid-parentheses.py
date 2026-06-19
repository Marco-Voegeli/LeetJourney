class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if not stack: 
                    return False
                last_bracket = stack.pop()
                if open_brackets[last_bracket] != c:
                    return False
        return not stack