class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_1 = 0
        p_2 = len(numbers) - 1
        while p_1 < p_2:
            score = numbers[p_1] + numbers[p_2] 
            if score == target:
                return [p_1 + 1, p_2 + 1]
            if score < target:
                p_1 += 1
            if score > target:
                p_2 -= 1
            