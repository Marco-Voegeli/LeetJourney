class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i-1] + nums[i]
            

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left-1] 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)               -2,  0, 3, -5,  2, -1
# param_1 = obj.sumRange(left,right) -2, -2, 1, -4, -2, -3