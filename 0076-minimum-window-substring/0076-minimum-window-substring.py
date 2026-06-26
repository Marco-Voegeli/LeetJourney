class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Move right pointer until all of t
        # Move left hand point until u hit a elem of t - record length
        # Move right pointer again until all of t
        t_counted = {}
        for c in t:
            if c not in t_counted:
                t_counted[c] = 1
            else:
                t_counted[c] += 1

        lhs = 0
        rhs = 0
        min_string = s + "a"

        while rhs != len(s):
            while rhs < len(s) and max(t_counted.values()) > 0:
                if s[rhs] in t_counted:
                    t_counted[s[rhs]] -= 1
                rhs += 1 
            while lhs < rhs and max(t_counted.values()) <= 0:
                if s[lhs] in t_counted:
                    t_counted[s[lhs]] += 1
                    new_substring = s[lhs:rhs] 
                    min_string = new_substring if len(new_substring) < len(min_string) else min_string
                lhs += 1
        return min_string if len(min_string) <= len(s) else ""
                
