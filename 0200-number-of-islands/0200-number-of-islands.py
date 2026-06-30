class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS search until we hit a 0; then we wait to till all threads hit 0; we flip those bits to 0 after and continue the BFS search.
        # First search; find first 1 then
        # Go through sides => [i+1, j], [i, j+1], [i+1, j + 1]; 
        # For each side: if == 0; return max_j and max_i -> gives us the range;
        # Once you hit a 0, return that j, and i => continue for min(j) and min(i)
        def bfs(i,j, grid: List[List[str]]) -> tuple(int, int):
            sides = [(i+u, j+v) for (u,v) in [(-1,0), (0, -1), (1, 0), (0, 1)]]
            for s_i, s_j in sides:
                if s_i < 0 or s_i >= len(grid) or s_j < 0 or s_j >= len(grid[0]):
                    continue
                val = grid[s_i][s_j]
                if val == "1":
                    grid[s_i][s_j] = "0"
                    bfs(s_i, s_j, grid)

        island = 0
        i = 0
        len_dim_2 = len(grid[i])
        while i < len(grid):
            j = 0
            while j < len_dim_2:
                if grid[i][j] == "1":
                    grid[i][j] = "0" # Flip when seen
                    island += 1
                    bfs(i, j, grid)
                j += 1
            i += 1
        return island