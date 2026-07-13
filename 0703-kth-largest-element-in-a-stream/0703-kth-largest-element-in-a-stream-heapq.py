import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val:int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

        
    def push(self, val:int) -> int:
        self.nums.append(val)
        i = len(self.nums) - 1
        while i > 0:
            parent_i = (i - 1) // 2 
            if self.nums[i] < self.nums[parent_i]:
                self.nums[i],self.nums[parent_i] = self.nums[parent_i], self.nums[i]
                i = parent_i
            else:
                break
        return self.nums[0]
    
    def pop(self) -> int:
        last = self.nums.pop()
        self.nums[0] = last
        i = 0
        while True:
            c_1, c_2 = 2*i+1, 2*i + 2
            child = i
            len_nums = len(self.nums)
            if c_1 < len_nums and self.nums[c_1] < self.nums[child]:
                child = c_1
            if c_2 < len_nums and self.nums[c_2] < self.nums[child]:
                child = c_2
            if child == i:
                break
            self.nums[i], self.nums[child] = self.nums[child], self.nums[i]
            i = child
        return self.nums[0]

    def add_manual(self, val: int) -> int:
        self.push(val)
        if len(self.nums) > self.k:
            return self.pop()
        return self.nums[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)