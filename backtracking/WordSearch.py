# https://neetcode.io/problems/search-for-word?list=neetcode150


class Solution:
    def __init__(self):
        self.board: list[list[str]] | None = None
        self.used: list[list[bool]] | None = None
        self.rowCount: int = -1
        self.columnCount: int = -1

    def _exist(self, row: int, column: int, word: str) -> bool:
        if not ((0 <= row < self.rowCount) and (0 <= column < self.columnCount)):
            return False
        if len(word) == 0:
            return False
        if word[0] == self.board[row][column] and not self.used[row][column]:
            self.used[row][column] = True
            if len(word) == 1:
                return True
            found = (
                self._exist(row, column + 1, word[1:])
                or self._exist(row, column - 1, word[1:])
                or self._exist(row + 1, column, word[1:])
                or self._exist(row - 1, column, word[1:])
            )
            if not found:
                self.used[row][column] = False
            return found
        else:
            return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board = board
        self.rowCount = len(board)
        self.columnCount = len(board[0])
        self.used = []
        for row in range(self.rowCount):
            self.used.append([False for _ in range(self.columnCount)])

        for row in range(len(board)):
            for column in range(len(board[row])):
                if self._exist(row, column, word):
                    return True
        return False
