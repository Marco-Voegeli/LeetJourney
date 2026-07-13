class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums_ordered = sorted(nums, reverse=True)
        self.nums = nums_ordered[:k]

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return self.nums[-1]
        if val <= self.nums[-1]:
            if len(self.nums) < self.k:
                self.nums.append(val)
                return val
            return self.nums[-1]
        for i, num in enumerate(self.nums):
            if val > num:
                self.nums[i+1:] = self.nums[i:max(self.k -1, len(self.nums)-1)] # Drop last elem
                self.nums[i] = val
                return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)