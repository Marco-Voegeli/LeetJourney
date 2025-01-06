class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for fast, _ in enumerate(nums):
            nums_fast = nums[fast]
            if nums_fast != val:
                nums[slow] = nums_fast
                slow += 1
        return slow