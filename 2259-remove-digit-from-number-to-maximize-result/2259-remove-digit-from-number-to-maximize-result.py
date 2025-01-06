class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        digit_idx = [i for i, a in enumerate(number) if number[i:i + len(digit)] == digit]
        digit_idx.sort()
        for idx in digit_idx:
            if len(number) == idx + 1:
                return number[:idx] + number[idx + 1:]
            print(number[idx+1])
            if number[idx+1] > number[idx]:
                return number[:idx] + number[idx + 1:]
        remov_idx = digit_idx[-1]
        return number[:remov_idx] + number[remov_idx + 1:]        