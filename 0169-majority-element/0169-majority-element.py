class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maj = 0
        for n in nums:
            if maj == 0:
                res = n
            maj += 1 if res == n else -1
        return res