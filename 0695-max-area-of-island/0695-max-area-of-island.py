from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        height = len(grid)
        width = len(grid[0])
        def bfs(y,x, grid):
            grid[y][x] = 0
            queue = deque([(y,x)])
            max_area = 0
            while queue:
                (a, b) = queue.pop()
                max_area += 1
                for (dy, dx) in directions:
                    (y, x) = (a + dy, b + dx)
                    if y < 0 or y >= height or x < 0 or x >= width:
                        continue
                    if grid[y][x] == 1:
                        grid[y][x] = 0
                        queue.append((y, x))
            return max_area
        i = 0
        res = 0
        while i < height:
            j = 0
            while j < width:
                if grid[i][j] == 1:
                    res = max(bfs(i,j, grid), res)
                j += 1
            i += 1
        return res