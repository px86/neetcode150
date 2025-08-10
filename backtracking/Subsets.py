# https://neetcode.io/problems/subsets?list=neetcode150


class Solution:
    def __init__(self):
        self.nums: list[int] | None = None
        self.solution: list[list[int]] = []
        self.current_set: list[int] | None = None

    def _subsets(self, index: int) -> None:
        if index == len(self.nums):
            self.solution.append(self.current_set.copy())
            return
        self.current_set.append(self.nums[index])
        self._subsets(index + 1)
        self.current_set.pop()
        self._subsets(index + 1)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.nums = nums
        self.solution = []
        self.current_set = []
        self._subsets(0)
        return self.solution
