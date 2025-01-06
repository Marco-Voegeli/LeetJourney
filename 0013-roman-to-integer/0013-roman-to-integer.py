class Solution:
    def romanToInt(self, s: str) -> int:
        if not str: return 0
        roman_dict = {'I':1, 'V':5,  'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        final_num = 0
        prev_c = ''
        for c in s:
            numer = roman_dict.get(c)
            final_num_temp = final_num
            if prev_c == 'I' and (c == 'V' or c == 'X'):
                final_num += numer - 2 # -(1 + 1) Removing the I added before, Because of the I put beforehand
            elif prev_c == 'X' and (c == 'L' or c == 'C'):
                final_num += numer - 20
            elif prev_c == 'C' and (c == 'M' or c == 'D'):
                final_num += numer - 200
            else:
                final_num += numer
            
            prev_c = c
        return final_num