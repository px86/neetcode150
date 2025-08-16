# https://neetcode.io/problems/counting-bits?list=neetcode150


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (1 << i) & n:
                count += 1
        return count

    def countBits(self, n: int) -> list[int]:
        solution = [0 for _ in range(n + 1)]
        for n in range(n + 1):
            solution[n] = self.hammingWeight(n)
        return solution
