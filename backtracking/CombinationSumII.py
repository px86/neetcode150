# https://neetcode.io/problems/combination-target-sum-ii?list=neetcode150

from typing import List


class Solution:
    def __init__(self):
        self.solutions = []
        self.freq = [0 for _ in range(51)]  # 1 <= candidates[i] <= 50

    def _recurs(self, i: int, current_set: List[int], target: int) -> None:
        # print(f"{i=}, {current_set=}, {target=}, {self.solutions=}")
        if i > target:
            return
        self._recurs(i + 1, current_set, target)  # taking the current number zero times
        if self.freq[i] == 0:
            return
        s = current_set.copy()
        for j in range(
            1, self.freq[i] + 1
        ):  # taking the current number 1...freq[num] times
            s.append(i)
            t = target - (j * i)
            if t == 0:
                self.solutions.append(s.copy())
                continue
            self._recurs(i + 1, s, target - (j * i))

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        for candidate in candidates:
            self.freq[candidate] += 1
        self._recurs(i=1, current_set=[], target=target)
        return self.solutions
