class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_house = 0
        prev_prev_house = 0
        for num in nums:
            temp_ = prev_house
            prev_house = max(num + prev_prev_house, temp_)
            prev_prev_house = temp_
        return max(prev_house, prev_prev_house)

