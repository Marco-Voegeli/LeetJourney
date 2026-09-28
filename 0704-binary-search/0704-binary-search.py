class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) 
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return m if l < r else -1
#[0, 5, 2] -> 3 == 9
#[2, 5, 3] -> 5 == 9
#[3, 5, 4] -> 9 == 9
