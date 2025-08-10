# https://neetcode.io/problems/combination-target-sum?list=neetcode150


class Solution:
    def __init__(self):
        self.nums: list[int] | None = None
        self.solutions: list[list[int]] | None = None
        self.current_set: list[list[int]] | None = None

    def _combinationSum(self, index: int, target: int):
        if index == len(self.nums):
            return

        if self.nums[index] == target:
            self.current_set.append(self.nums[index])
            self.solutions.append(self.current_set.copy())
            self.current_set.pop()

        elif self.nums[index] < target:
            self.current_set.append(self.nums[index])
            self._combinationSum(index, target - self.nums[index])
            self.current_set.pop()

        self._combinationSum(index + 1, target)

    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        self.nums = nums
        self.solutions = []
        self.current_set = []
        self._combinationSum(0, target)
        return self.solutions
