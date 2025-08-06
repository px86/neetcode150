# https://neetcode.io/problems/subsets?list=neetcode150

from typing import List


class Solution:
    def __init__(self):
        self.all_subsets = []

    def _subsets(self, nums, current_set):
        if len(nums) == 0:
            self.all_subsets.append(current_set)
            return
        s1 = current_set.copy()
        self._subsets(nums[1:], s1)
        s2 = current_set.copy()
        s2.append(nums[0])
        self._subsets(nums[1:], s2)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.all_subsets = []
        self._subsets(nums, [])
        return self.all_subsets
