# https://neetcode.io/problems/kth-largest-element-in-an-array?list=neetcode150

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k:
                if heap[0] < num:
                    heapq.heappushpop(heap, num)
                else:
                    pass
            else:
                heapq.heappush(heap, num)
        return heap[0]
