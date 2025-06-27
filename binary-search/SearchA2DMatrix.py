# https://neetcode.io/problems/search-2d-matrix?list=neetcode150
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m))
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid + 1][0] > target:
                left = mid
                break
            else:
                left = mid + 1

        # O(log(n))
        array = matrix[left]
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            if array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
