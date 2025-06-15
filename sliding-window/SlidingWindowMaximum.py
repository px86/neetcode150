# https://neetcode.io/problems/sliding-window-maximum?list=neetcode150

import typing


class IndexedInt:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index

    def __gt__(self, other) -> bool:
        if self.value > other.value:
            return True
        return False


IntType: typing.TypeAlias = int | IndexedInt


class MaxHeap:
    def __init__(self, heap: typing.Optional[typing.List[IntType]] = None):
        self.heap: typing.List[IntType] = [] if heap is None else heap
        if heap is not None:
            self.heapify()

    def heapify_down(self, index: int):
        node = index
        while node < len(self.heap):
            left = 2 * node + 1
            right = 2 * node + 2

            if left >= len(self.heap):
                break

            elif right >= len(self.heap):
                if self.heap[left] > self.heap[node]:
                    self.heap[node], self.heap[left] = (
                        self.heap[left],
                        self.heap[node],
                    )
                else:
                    break

            else:
                if self.heap[left] > self.heap[right]:
                    if self.heap[left] > self.heap[node]:
                        self.heap[node], self.heap[left] = (
                            self.heap[left],
                            self.heap[node],
                        )
                        node = left
                    else:
                        break

                else:
                    if self.heap[right] > self.heap[node]:
                        self.heap[node], self.heap[right] = (
                            self.heap[right],
                            self.heap[node],
                        )
                        node = right
                    else:
                        break

    def heapify(self):
        for i in range(len(self.heap) - 1, -1, -1):
            self.heapify_down(index=i)

    def insert(self, el: int):
        self.heap.append(el)
        node = len(self.heap) - 1
        parent = (node - 1) // 2
        while parent >= 0:
            if self.heap[node] > self.heap[parent]:
                self.heap[node], self.heap[parent] = self.heap[parent], self.heap[node]
                node = parent
                parent = (node - 1) // 2
            else:
                break

    def delete(self) -> IntType | None:
        if len(self.heap) == 0:
            return None
        element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 1:
            self.heapify_down(index=0)
        return element


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxheap = MaxHeap()
        for i in range(k):
            maxheap.insert(IndexedInt(index=i, value=nums[i]))

        maxsinwin = [maxheap.heap[0].value]

        for i in range(1, len(nums) - k + 1):
            if nums[i - 1] == maxheap.heap[0].value:
                maxheap.delete()
            maxheap.insert(IndexedInt(index=i + k - 1, value=nums[i + k - 1]))
            while maxheap.heap[0].index < i:
                maxheap.delete()
            maxsinwin.append(maxheap.heap[0].value)

        return maxsinwin
