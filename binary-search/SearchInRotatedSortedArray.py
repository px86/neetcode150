# https://neetcode.io/problems/find-target-in-rotated-sorted-array?list=neetcode150

from typing import List


class Solution:

    def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> int:
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return index

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        index = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if left == mid:
                if nums[left] == target:
                    index = left
                elif nums[right] == target:
                    index = right
                break
            # When left partition is sorted
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    index = self.binarySearch(nums, left, mid, target)
                    break
                else:
                    left = mid
            # When left partition is not sorted, which means right partition is sorted
            else:
                if nums[mid] <= target <= nums[right]:
                    index = self.binarySearch(nums, mid, right, target)
                    break
                else:
                    right = mid

        return index
