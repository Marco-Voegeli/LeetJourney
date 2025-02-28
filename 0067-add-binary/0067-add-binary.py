class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pad_len = abs(len(a) - len(b))
        if len(a) > len(b):
            b = "0"*pad_len + b
        else:
            a = "0" * pad_len + a
        carry = 0
        res = len(a)*[0]
        for i in range(len(a)-1,-1,-1):
            b_res = int(a[i]) + int(b[i]) + carry
            res[i] = b_res % 2
            carry = b_res // 2
        if carry:
            res = [1] + res
        return "".join(str(x) for x in res)


