class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0 : 1} # prefix sum: freq
        res_counter = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            residual = prefix_sum - k
            if residual in sum_dict:
                res_counter += sum_dict[residual]
            if prefix_sum in sum_dict:
                sum_dict[prefix_sum] += 1
            else:
                sum_dict[prefix_sum] = 1
        return res_counter
            