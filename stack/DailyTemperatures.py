# https://neetcode.io/problems/daily-temperatures?list=neetcode150

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while len(stack) and stack[-1][0] < temperatures[i]:
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        return output
