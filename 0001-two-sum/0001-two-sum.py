class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1 
        nums_idx = [(num ,i) for (i, num) in enumerate(nums)]
        list.sort(nums_idx)
        output = nums_idx[p1][0] + nums_idx[p2][0]
        while output != target:
            if output > target:
                p2 -= 1
            elif output < target:
                p1 += 1
            output = nums_idx[p1][0] + nums_idx[p2][0]
        return  [nums_idx[p1][1], nums_idx[p2][1]]
