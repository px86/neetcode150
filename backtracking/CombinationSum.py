# https://neetcode.io/problems/combination-target-sum?list=neetcode150

from typing import List


class Solution:
    def __init__(self):
        self.solutions = []

    def _combinationSum(self, nums, current_set, target):
        # print(f"{nums=}, {current_set=}, {target=}")
        if len(nums) == 0:
            return

        if nums[0] == target:
            solution = current_set.copy()
            solution.append(nums[0])
            self.solutions.append(solution)
            return self._combinationSum(nums[1:], current_set, target)

        if nums[0] < target:
            s1 = current_set.copy()
            s1.append(nums[0])
            self._combinationSum(nums, s1, target - nums[0])

        s2 = current_set.copy()
        self._combinationSum(nums[1:], s2, target)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.solutions = []
        self._combinationSum(nums, [], target)
        return self.solutions
