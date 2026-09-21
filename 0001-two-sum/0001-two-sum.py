class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1 
        nums_idx = [(num ,i) for (i, num) in enumerate(nums)]
        list.sort(nums_idx)
        while p1 < p2:
            num_1, idx_1 = nums_idx[p1]
            num_2, idx_2 = nums_idx[p2]
            output = num_1 + num_2
            if output == target:
                return [idx_1, idx_2]
            elif output > target:
                p2 -= 1
            elif output < target:
                p1 += 1
        raise "no solution found"
            

