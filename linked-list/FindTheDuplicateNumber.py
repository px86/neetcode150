# https://neetcode.io/problems/find-duplicate-integer?list=neetcode150

from typing import List


class Solution:

    # Naive solution
    #
    # def findDuplicate(self, nums: List[int]) -> int:
    #     domain = [False for i in range(10000)]
    #     for num in nums:
    #         if domain[num - 1]:
    #             return num
    #         else:
    #             domain[num - 1] = True

    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                return abs(num)
            nums[index] *= -1
