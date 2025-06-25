# https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            count = 1
            while len(stack) and stack[-1][0] > heights[i]:
                last_tallest = stack.pop()
                if len(stack):
                    area = last_tallest[0] * (i - stack[-1][1] - 1)
                else:
                    area = last_tallest[0] * i
                if area > max_area:
                    max_area = area
            stack.append((heights[i], i))

        while len(stack):
            value = stack.pop()[0]
            if len(stack):
                value *= len(heights) - stack[-1][1] - 1
            else:
                value *= len(heights)
            if value > max_area:
                max_area = value
        return max_area
