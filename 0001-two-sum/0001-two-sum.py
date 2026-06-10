class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda item: item[1])
        lhs_i = 0
        rhs_i = len(sorted_nums) - 1
        curr_val = sorted_nums[lhs_i][1] + sorted_nums[rhs_i][1]
        while curr_val != target:
            if curr_val < target:
                lhs_i = lhs_i + 1
            else:
                rhs_i = rhs_i - 1
            curr_val = sorted_nums[lhs_i][1] + sorted_nums[rhs_i][1]
        return [sorted_nums[lhs_i][0], sorted_nums[rhs_i][0]]