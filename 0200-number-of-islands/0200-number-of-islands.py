from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j, grid):
            queue = deque()
            sides = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for (di, dj) in sides:
                if i + di < 0 or i + di >= m:
                    continue
                if j + dj < 0 or j + dj >= n:
                    continue
                if grid[i+di][j+dj] == "1":
                    queue.append((i+di, j + dj))
                
            while queue:
                (i,j) = queue.popleft()
                grid[i][j] = '0'
                bfs(i, j, grid)
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    bfs(i, j, grid)
                    res += 1
        return res 
        