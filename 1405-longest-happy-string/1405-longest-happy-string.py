class Solution:
    
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def remove_char(a, b, c, new_c):
            if new_c == 'a':
                return a-1, b, c
            if new_c == 'b':
                return a, b-1, c
            if new_c == 'c':
                return a, b, c-1
        def rec_func(a, b, c, res): 
            if a == 0 and b == 0 and c == 0:
                return 0, 0, 0, res
            ls = [(a, 0 , 'a'), (b, 1, 'b'), (c, 2, 'c')]
            ls.sort(reverse = True)
            new_c = ''
            if len(res) >= 2:
                if res[-2] == res[-1] == ls[0][2]:
                    if ls[1][0] == 0:
                        return 0, 0, 0, res
                    else:
                        new_c = ls[1][2]
                else:
                    new_c = ls[0][2]
            else:
                if ls[0][0] == 0:
                    return 0, 0, 0, res
                else:
                    new_c = ls[0][2]    
            a_new, b_new, c_new = remove_char(a,b, c, new_c) 
            return rec_func(a_new, b_new, c_new, res + new_c)
        a,b,c,res = rec_func(a,b,c, '')
        return res