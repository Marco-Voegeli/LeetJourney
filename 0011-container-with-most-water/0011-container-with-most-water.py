class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(x_1, x_2):
            y_1 = height[x_1]
            y_2 = height[x_2]
            return (x_2 - x_1) * min(y_1, y_2)
        lhs = 0
        rhs = len(height) - 1
        max_area = 0
        while lhs < rhs:
            max_area = max(max_area, area(lhs, rhs))
            if height[lhs] > height[rhs]:
                rhs -= 1
            else:
                lhs += 1
        return max_area
                
