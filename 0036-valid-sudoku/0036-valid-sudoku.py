class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # col, row
        for i in range(9):
            set_row = set()
            set_col = set()
            for j in range(9):
                val_row = board[i][j]
                val_col = board[j][i]
                if val_row != ".":
                    if val_row in set_row:
                        return False
                    set_row.add(val_row)
                if val_col != ".":
                    if val_col in set_col:
                        return False
                    set_col.add(val_col)
        for j in range(3):
            for i in range(3):
                square = board[i*3:i*3 + 3]
                square_ls = [x for x in square[0][3*j: 3*(j+1)] if x!= "."]
                for row in square[1:]:
                    square_ls.extend([x for x in row[3*j: 3*(j+1)] if x != "."])
                if len(square_ls) != len(set(square_ls)):
                    return False
        return True