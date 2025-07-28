# https://neetcode.io/problems/last-stone-weight?list=neetcode150

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [-w for w in stones]
        heapq.heapify(weights)
        while len(weights) > 1:
            x, y = -1 * heapq.heappop(weights), -1 * heapq.heappop(weights)
            if x != y:
                heapq.heappush(weights, -1 * abs(x - y))
        return -1 * weights[0] if len(weights) else 0
