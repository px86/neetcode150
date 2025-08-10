# https://neetcode.io/problems/combination-target-sum-ii?list=neetcode150


class Solution:
    def __init__(self):
        self.current_set: list[int] | None = None
        self.solutions: list[list[int]] | None = None
        self.freq: list[int] = [0 for _ in range(51)]  # 1 <= candidates[i] <= 50

    def _recurs(self, num: int, target: int) -> None:
        # print(f"{i=}, {current_set=}, {target=}, {self.solutions=}")
        if num > target:
            return
        # taking the current number zero times
        self._recurs(num + 1, target)
        if self.freq[num] == 0:
            return
        # taking the current number 1...freq[num] times
        for j in range(1, self.freq[num] + 1):
            self.current_set.append(num)
            t = target - (j * num)
            if t == 0:
                self.solutions.append(self.current_set.copy())
                continue
            self._recurs(num + 1, target - (j * num))
        for j in range(1, self.freq[num] + 1):
            self.current_set.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.current_set = []
        self.solutions = []
        for candidate in candidates:
            self.freq[candidate] += 1
        self._recurs(1, target)
        return self.solutions
