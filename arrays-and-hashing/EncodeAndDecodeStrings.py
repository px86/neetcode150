# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append(s)
        return ",".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while True:
            j = s.find(",", i)
            if j == -1:
                break
            else:
                length = int(s[i:j])
                result.append(s[j + 1 : j + 1 + length])
                i = j + length + 2
        return result
