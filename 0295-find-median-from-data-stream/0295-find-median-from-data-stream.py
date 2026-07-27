import heapq
class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.l_size = 0
        self.r_size = 0
        heapq.heapify_max(self.left_heap)
        heapq.heapify(self.right_heap)

    def addNum(self, num: int) -> None:
        # Add num to the correct heap; then if unbalanced pop element and add to the other heap
        # If it's first elem add to right heap
        if not self.right_heap:
            heapq.heappush(self.right_heap, num)
            self.r_size += 1
            return

        # Compare num to first elem of self.right_heap:
        if self.right_heap[0] > num:
            heapq.heappush_max(self.left_heap, num)
            self.l_size += 1
        else:
            heapq.heappush(self.right_heap, num)
            self.r_size += 1

        # Sort heaps and compare sizes
        if self.l_size > self.r_size + 1:
            # Rebalance right side
            heapq.heappush(self.right_heap,heapq.heappop_max(self.left_heap))
            self.r_size += 1
            self.l_size -= 1
            return
        if self.r_size > self.l_size + 1:
            heapq.heappush_max(self.left_heap,heapq.heappop(self.right_heap))
            self.l_size += 1
            self.r_size -= 1
            return
            
    def findMedian(self) -> float:
        if (self.l_size + self.r_size) % 2 == 0:
            return (self.right_heap[0] + self.left_heap[0]) / 2
        else:
            return self.right_heap[0] if self.r_size > self.l_size else self.left_heap[0] 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()