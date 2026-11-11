class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        paths = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # dfs type recursion

        def dfs(i, j, sub_word, explored):
            if not sub_word:
                return True
            res = False
            for (d_x, d_y) in paths:
                i_d_x = i + d_x
                j_d_y = j + d_y
                if i_d_x >= 0 and i_d_x < m and j_d_y >= 0 and j_d_y < n:
                    if not explored[i_d_x][j_d_y] and board[i_d_x][j_d_y] == sub_word[0]:
                        explored[i_d_x][j_d_y] = True

                        res = res or dfs(i_d_x, j_d_y, sub_word[1:], explored)
                        if not res:
                            explored[i_d_x][j_d_y] = False                        
                if res:
                    break
            return res
        res = False
        for i in range(m):
            for j in range(n):
                if res:
                    return True
                if board[i][j] == word[0]:
                    explored = [[False for _ in range(n)] for _ in range(m)]
                    explored[i][j] = True
                    res = res or dfs(i, j, word[1:], explored)
        return res


