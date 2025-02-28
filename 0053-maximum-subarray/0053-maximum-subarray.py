class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxi = -10**4
        for i in range(len(nums)):
            if s < 0:
                s = 0
            s += nums[i]
            if s > maxi:
                maxi = s
        return maxi
