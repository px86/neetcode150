# https://neetcode.io/problems/max-water-container?list=neetcode150

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = -1
        while left < right:
            width = right - left
            if heights[left] > heights[right]:
                area = heights[right] * width
                right -= 1
            else:
                area = heights[left] * width
                left += 1
            if area > max_area:
                max_area = area
        return max_area
