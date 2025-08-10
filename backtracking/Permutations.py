# https://neetcode.io/problems/permutations?list=neetcode150

from typing import List, Optional


class Solution:

    def __init__(self):
        self.permutations = []
        self.nums: Optional[List[int]] = None
        self.current_permutation = []
        self.bitmap = None

    def _permute(self, index: int):
        if index == len(self.bitmap):
            self.permutations.append(self.current_permutation.copy())
            return
        for j in range(len(self.bitmap)):
            if self.bitmap[j]:
                continue
            self.bitmap[j] = True
            self.current_permutation.append(self.nums[j])
            self._permute(index + 1)
            self.bitmap[j] = False
            self.current_permutation.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.current_permutation = []
        self.bitmap = [False for _ in range(len(nums))]
        self._permute(0)
        return self.permutations
