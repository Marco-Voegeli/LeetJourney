class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n_half = (len(nums)+1) // 2 - 1
        counter = 0
        num_focus = nums[0]
        for num in nums:
            if num == num_focus:
                counter += 1
                if counter > n_half:
                    return num_focus
            else:
                num_focus = num
                counter = 1
        return num_focus