# https://neetcode.io/problems/subsets-ii?list=neetcode150


class Solution:

    def __init__(self):
        self.current_set: list[int] | None = None
        self.solutions: list[list[int]] | None = None
        self.freq: list[int] = [0 for _ in range(51)]
        self.nums: list[int] | None = None

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.current_set = []
        self.solutions = []
        nums.sort()
        self.nums = nums
        for num in nums:
            self.freq[num + 20] += 1
        self._subsets(0)
        return self.solutions

    def _subsets(self, index: int) -> None:
        # print(f"{index=}, {self.current_set=}, {self.solutions=}")
        if index >= len(self.nums):
            self.solutions.append(self.current_set.copy())
            return
        num = self.nums[index]
        freq = self.freq[num + 20]
        self._subsets(index + freq if freq else 1)
        for i in range(freq):
            self.current_set.append(num)
            self._subsets(index + freq if freq else 1)
        for i in range(freq):
            self.current_set.pop()
