# https://neetcode.io/problems/eating-bananas?list=neetcode150

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rates = range(1, max(piles) + 1)
        solution = rates[-1]
        left = 0
        right = len(rates)
        while left <= right:
            mid = (left + right) // 2
            time_taken = 0
            for pile in piles:
                time_taken += pile // rates[mid]
                if pile % rates[mid]:
                    time_taken += 1
            if time_taken > h:
                left = mid + 1
            else:
                solution = rates[mid]
                right = mid - 1
        return solution
