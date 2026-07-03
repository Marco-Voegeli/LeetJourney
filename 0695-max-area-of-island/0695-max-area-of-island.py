from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        height = len(grid)
        width = len(grid[0])
        def bfs(y,x, grid):
            if grid[y][x] == 0:
                return 0
            queue = deque()
            for (dy, dx) in directions:
                if y+dy < 0 or y+dy >= height or x+dx < 0 or x+dx >= width:
                    continue
                if grid[y+dy][x+dx] == 1:
                    queue.append((y + dy, x + dx))
            grid[y][x] = 0
            max_area = 1
            while queue:
                (y, x) = queue.pop()
                max_area += bfs(y,x,grid)
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