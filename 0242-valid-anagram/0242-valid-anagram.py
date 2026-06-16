class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def add_c(c, base_map):
            if c in base_map:
                base_map[c] += 1
            else:
                base_map[c] = 1
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for (s_c, t_c) in zip(s,t):
            add_c(s_c, s_map)
            add_c(t_c, t_map)
        if s_map == t_map:
            return True
        else:
            return False


        