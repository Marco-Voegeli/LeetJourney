from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def explore(x, y):
            if x >= m or x < 0:
                return 0
            if y >= n or y < 0:
                return 0
            if grid[x][y] == '0':
                return 0 
            else:
                grid[x][y] = '0'
                explore(x+1, y)
                explore(x, y+1)
                explore(x-1, y)
                explore(x, y-1)
                return 1

        res = 0
        for i in range(m):
            for j in range(n):
                res += explore(i, j)

        return res


        [["1","1","1"],
         ["0","1","0"],
         ["1","1","1"]]



                    
                    