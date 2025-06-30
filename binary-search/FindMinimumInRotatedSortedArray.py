# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array?list=neetcode150

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if left == mid or right == mid:
                return min(nums[left], nums[right])
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
