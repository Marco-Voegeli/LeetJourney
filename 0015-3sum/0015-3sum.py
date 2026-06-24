class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set = set()
        sorted_nums = sorted(nums)
        print(sorted_nums)
        for i, num in enumerate(sorted_nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                num_j = sorted_nums[j]
                num_k = sorted_nums[k]
                sum_zero = num_j + num_k + num 
                if sum_zero == 0:
                    result_set.add((num, num_j, num_k))
                    j += 1
                    k -= 1
                if sum_zero < 0 :
                    j += 1
                if sum_zero > 0:
                    k -= 1
        return list(result_set)
                


