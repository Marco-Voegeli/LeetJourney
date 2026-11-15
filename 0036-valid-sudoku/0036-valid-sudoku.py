class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # col, row
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                box = (i//3, j // 3)
                if v in rows[i] or v in cols[j] or v in boxes[box]:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                boxes[box].add(v)
        return True
