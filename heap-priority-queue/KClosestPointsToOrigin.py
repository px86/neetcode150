# https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150

import math
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.sqrt(p[0] ** 2 + p[1] ** 2), p) for p in points]
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
