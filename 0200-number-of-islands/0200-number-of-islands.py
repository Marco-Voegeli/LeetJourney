from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS search until we hit a 0; then we wait to till all threads hit 0; we flip those bits to 0 after and continue the BFS search.
        # First search; find first 1 then
        # Go through sides => [i+1, j], [i, j+1], [i+1, j + 1]; 
        # For each side: if == 0; return max_j and max_i -> gives us the range;
        # Once you hit a 0, return that j, and i => continue for min(j) and min(i)
        def dfs(i,j, grid: List[List[str]]) -> tuple(int, int):
            sides = [(i+u, j+v) for (u,v) in [(-1,0), (0, -1), (1, 0), (0, 1)]]
            for s_i, s_j in sides:
                if s_i < 0 or s_i >= len(grid) or s_j < 0 or s_j >= len(grid[0]):
                    continue
                val = grid[s_i][s_j]
                if val == "1":
                    grid[s_i][s_j] = "0"
                    bfs(s_i, s_j, grid)
        island = 0
        height = len(grid)
        width = len(grid[0])
        def bfs(i, j, grid: List[List[str]]) -> None:
            sides = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            queue = deque()
            grid[i][j] = "0"
            for (dx, dy) in sides:
                if i +dx < 0 or i + dx >= height:
                    continue 
                if j + dy < 0 or j + dy >= width:
                    continue
                if grid[i+dx][j+dy] == "1":
                    queue.append((i+dx, j+dy))
            while queue:
                (x, y) = queue.popleft()
                bfs(x, y, grid)
            

        i = 0
        while i < len(grid):
            j = 0
            while j < width:
                if grid[i][j] == "1":
                    island += 1
                    bfs(i, j, grid)
                j += 1
            i += 1
        return island