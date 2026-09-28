from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        res = 0
        m = len(grid)
        n = len(grid[0])
        def bfs(i, j, grid) -> None:
            sides = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            queue = deque()
            grid[i][j] = '0'    
            for dx, dy in sides:
                if i + dx < 0 or i + dx >= m:
                    continue
                if j + dy < 0 or j + dy >= n:
                    continue
                if grid[i+dx][j+dy] == '1':
                    queue.append((i+dx,j+dy))
        
            while queue:
                (i, j) = queue.popleft()
                bfs(i, j, grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j, grid)
        return res