# https://neetcode.io/problems/task-scheduling?list=neetcode150

import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0 for _ in range(26)]
        for task in tasks:
            freq[ord(task) - ord("A")] -= 1
        heap = [f for f in freq if f]
        heapq.heapify(heap)
        queue = []
        t = 0
        while len(heap) or len(queue):
            t += 1
            if len(queue) and queue[0][1] <= t:
                heapq.heappush(heap, queue.pop(0)[0])
            if len(heap):
                task = heapq.heappop(heap)
                task += 1
                if task:
                    queue.append((task, t + n + 1))
        return t
