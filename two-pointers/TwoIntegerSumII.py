# https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150

from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]  # 1 based index
            elif sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]
