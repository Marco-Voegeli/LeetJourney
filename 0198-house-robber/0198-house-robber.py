class Solution:
    def rob(self, nums: List[int]) -> int:
        # Two cases: We either rob the first or the second house
        # And we can keep going like this until we only have two houses
        # Where we rob the house with the most amount of money
        if not nums:
            return [0]
        if len(nums) < 2:
            return nums[0]
        memoiz = [nums[0], max(nums[0], nums[1])]
        i = 0
        for i in range(2, len(nums)):
            memoiz.append(max(nums[i] + memoiz[i-2], memoiz[i-1]))
        
        return memoiz[-1]