class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counter = {}
        n_half = len(nums) // 2 # Floored
        for num in nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1
        return max(num_counter, key=num_counter.get)