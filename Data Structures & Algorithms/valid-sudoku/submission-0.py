class Solution:
    def isValidSudoku(self, board):

        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                num = int(board[r][c]) - 1

                box = (r // 3) * 3 + (c // 3)

                if rows[r][num]:
                    return False

                if cols[c][num]:
                    return False

                if boxes[box][num]:
                    return False

                rows[r][num] = True
                cols[c][num] = True
                boxes[box][num] = True

        return True