# https://neetcode.io/problems/find-median-in-a-data-stream?list=neetcode150

import heapq


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if len(self.max_heap) == 0 or num <= -1 * self.max_heap[0]:
                heapq.heappush(self.max_heap, -1 * num)
            else:
                heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) > len(self.min_heap):
            if num <= -1 * self.max_heap[0]:
                heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -1 * num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num >= self.min_heap[0]:
                heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -1 * num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -1 * self.max_heap[0]
