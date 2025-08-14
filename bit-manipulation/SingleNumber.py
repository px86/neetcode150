# https://neetcode.io/problems/single-number?list=neetcode150


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
