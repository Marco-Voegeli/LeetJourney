class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            return 0 if nums[0] == target else -1
        if nums[length // 2] == target:
            return mid
        if nums[length // 2] > target:
            res = self.search(nums[:mid], target)
            return -1 if res < 0 else res
        if nums[length // 2] < target:
            res = self.search(nums[mid:], target)
            return -1 if res < 0 else res + mid
        return -1
            