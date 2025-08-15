# https://neetcode.io/problems/number-of-one-bits?list=neetcode150


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (1 << i) & n:
                count += 1
        return count
