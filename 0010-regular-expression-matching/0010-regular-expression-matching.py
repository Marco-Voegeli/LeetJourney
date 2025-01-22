class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(pp, ps): 
            '''
            pp: pointer for pattern p
            ps: pointer for string s
            '''
            while pp >= 0:
                if p[pp] == '*':
                    prev_p = p[pp - 1]
                    while ps >= 0 and (s[ps] == prev_p or prev_p  == '.'):
                        if dfs(pp-2, ps):
                            return True
                        ps -= 1
                    pp -= 2 # The * char and the repeated char
                elif ps < 0:
                    return False
                elif p[pp] == s[ps]:
                    pp -= 1
                    ps -= 1
                elif p[pp] == '.':
                    pp -= 1
                    ps -= 1
                else:
                    return False
            return ps == -1 and pp == -1
        return dfs(len(p) - 1, len(s) - 1)