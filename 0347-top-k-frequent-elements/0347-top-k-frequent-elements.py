class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # mst required of k elements
        # when a new element arrives you place it at the top
        nums.sort()
        num_freq = []
        i = 0
        while i < len(nums):
            i_elem = nums[i]
            j = i
            while j < len(nums) and nums[j] == i_elem:
                j += 1
            heappush_max(num_freq, (j - i, i_elem))
            i = j
        res = []
        for i in range(k):
            res.append(heappop_max(num_freq)[1])
    
        return res