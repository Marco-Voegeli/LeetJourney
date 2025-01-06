class Solution:
    def stringSequence(self, target: str) -> List[str]:
        def press_key2(curr_str, res_ls):
            last_char = ord(curr_str[-1]) + 1
            curr_str = curr_str[:-1] + chr(last_char)
            res_ls.append(curr_str)
            return curr_str

        res_ls = []
        curr_str = ''
        for let in target:
            curr_str += 'a'
            res_ls.append(curr_str)
            while curr_str[-1] != let:
                curr_str = press_key2(curr_str, res_ls)
        return res_ls