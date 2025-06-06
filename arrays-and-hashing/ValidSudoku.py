# https://neetcode.io/problems/valid-sudoku?list=neetcode150


class Solution:
    def allUnique(self, nums: List[str]) -> bool:
        collection = set()
        for n in nums:
            if n == ".":
                continue
            num = int(n)
            if num in collection:
                return False
            collection.add(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # verify rows
        for row in board:
            if not self.allUnique(row):
                return False

        # verify columns
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not self.allUnique(col):
                return False

        # verify each box
        indicies = (
            (0, 0),
            (0, 3),
            (0, 6),
            (3, 0),
            (3, 3),
            (3, 6),
            (6, 0),
            (6, 3),
            (6, 6),
        )

        for indx in indicies:
            i, j = indx
            box = [
                board[i][j],
                board[i][j + 1],
                board[i][j + 2],
                board[i + 1][j],
                board[i + 1][j + 1],
                board[i + 1][j + 2],
                board[i + 2][j],
                board[i + 2][j + 1],
                board[i + 2][j + 2],
            ]
            if not self.allUnique(box):
                return False

        return True
