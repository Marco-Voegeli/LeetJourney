import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.kthLargest = nums
        self.k = k
        heapq.heapify(self.kthLargest)
        while len(self.kthLargest) > k:
            heapq.heappop(self.kthLargest)

    def add(self, val: int) -> int:
        if not self.kthLargest or len(self.kthLargest) < self.k:
            heapq.heappush(self.kthLargest, val)
            return self.kthLargest[0]
        if val > self.kthLargest[0]:
            heapq.heappushpop(self.kthLargest, val)
        return self.kthLargest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)