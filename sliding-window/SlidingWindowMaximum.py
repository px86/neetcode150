# https://neetcode.io/problems/sliding-window-maximum?list=neetcode150

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        solution = []
        maximum = -1001
        imaximum = -1
        for l in range(len(nums) - k + 1):
            r = l + k - 1
            if l <= imaximum <= r:
                if nums[r] >= maximum:
                    maximum = nums[r]
                    imaximum = r
                else:
                    pass
            else:
                maximum = nums[l]
                imaximum = l
                for i in range(l + 1, r + 1):
                    if nums[i] >= maximum:
                        maximum = nums[i]
                        imaximum = i
            solution.append(maximum)
        return solution
