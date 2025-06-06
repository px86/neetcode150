# https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_lcs = {}
        for num in nums:
            num_lcs[num] = False

        lcs = 0
        for num in nums:
            if num_lcs[num]:
                continue
            low = high = num
            while low - 1 in num_lcs:
                num_lcs[low - 1] = True
                low -= 1
            while high + 1 in num_lcs:
                num_lcs[high + 1] = True
                high += 1
            span = high - low + 1
            if span > lcs:
                lcs = span
        return lcs
