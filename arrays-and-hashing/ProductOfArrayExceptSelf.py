# https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lhs = [
            1,
        ] * len(nums)
        for i in range(1, len(nums)):
            lhs[i] = lhs[i - 1] * nums[i - 1]

        rhs = [
            1,
        ] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            rhs[i] = rhs[i + 1] * nums[i + 1]

        result = [lhs[i] * rhs[i] for i in range(len(nums))]
        return result
