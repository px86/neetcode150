# https://neetcode.io/problems/three-integer-sum?list=neetcode150

from typing import List
import bisect


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -1 * num1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum == target:
                    num2 = nums[j]
                    num3 = nums[k]
                    solution.append([num1, num2, num3])
                    while j < k and nums[j] == num2:
                        j += 1
                    while j < k and nums[k] == num3:
                        k -= 1
                elif sum > target:
                    k -= 1
                else:
                    j += 1

        return solution
