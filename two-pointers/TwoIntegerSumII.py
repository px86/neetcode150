# https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150

import bisect


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            difference = target - num
            j = bisect.bisect_left(numbers, difference, lo=i + 1)
            if j != len(numbers) and numbers[j] == difference:
                return [i + 1, j + 1]
        return [-1, -1]
