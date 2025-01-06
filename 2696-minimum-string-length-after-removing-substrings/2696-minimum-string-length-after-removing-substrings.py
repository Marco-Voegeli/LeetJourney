class Solution:
    def minLength(self, s: str) -> int:
        ab = "AB"
        cd = "CD"
        updating_src = [c for c in s]
        p1 = 0
        if len(s) < 2:
            return len(s)
        while p1 < len(updating_src) - 1:
            pair = updating_src[p1] + updating_src[p1 + 1]
            if pair == ab or pair == cd:
                updating_src = updating_src[:p1] + updating_src[p1 + 2:]
                if p1 > 0:
                    p1 -= 1
            else:
                p1 += 1
            
        return len(updating_src)