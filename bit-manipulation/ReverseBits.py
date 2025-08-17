# https://neetcode.io/problems/reverse-bits?list=neetcode150


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if n & (1 << (31 - i)):
                result |= 1 << i
        return result
