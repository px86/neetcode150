# https://neetcode.io/problems/time-based-key-value-store?list=neetcode150

from typing import Dict, Tuple, List


class TimeMap:

    def __init__(self):
        self.store: Dict[str, List[Tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        solution = ""
        values = self.store[key]
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                solution = values[m][0]
                l = m + 1
        return solution
