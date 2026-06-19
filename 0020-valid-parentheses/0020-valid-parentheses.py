class Solution:
    def isValid(self, s: str) -> bool:
        paren = [0,0,0] # (), [], {}
        open_brackets = {'[': ']', '{': '}', '(': ')'}
        heap = []
        for c in s:
            if c in open_brackets:
                heap.append(c)
            if c in open_brackets.values():
                if not heap: 
                    return False
                last_bracket = heap.pop()
                if last_bracket not in open_brackets or open_brackets[last_bracket] != c:
                    return False
        if not heap:
            return True
        else:
            return False