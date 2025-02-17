class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while(lo < hi):
            mid = lo + (hi - lo + 1)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                lo = mid
            if target < nums[mid]:
                hi = mid - 1
        return -1 if nums[lo] != target else lo