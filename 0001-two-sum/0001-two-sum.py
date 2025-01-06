class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_map = {}
        for i, num in enumerate(nums):
            new_target = target-num

            if new_target in number_map:
                return [i, number_map[new_target]]
            number_map[num]= i
        return None