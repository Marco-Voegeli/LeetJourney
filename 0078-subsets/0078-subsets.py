class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = [[]]
        for num in nums:
            queue = []
            for out in output:
                queue.append(out + [num])
            output.extend(queue)
        return output