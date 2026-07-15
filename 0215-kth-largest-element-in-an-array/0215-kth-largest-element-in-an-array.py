class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        list.sort(nums)
        return nums[-k]