# https://neetcode.io/problems/sum-of-two-integers?list=neetcode150


class Solution:
    def getSumOfUnsigned(self, a: int, b: int) -> int:
        carry_bit = 0
        sum = 0
        for i in range(32):
            mask = 1 << i
            a_bit = (a & mask) >> i
            b_bit = (b & mask) >> i
            if a_bit ^ b_bit ^ carry_bit:
                sum |= 1 << i
            if (a_bit & b_bit) | (a_bit & carry_bit) | (b_bit & carry_bit):
                carry_bit = 1
            else:
                carry_bit = 0
        return sum

    def getSum(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0:
            return self.getSumOfUnsigned(a, b)
        elif a >= 0:
            # b is negative
            pass
        elif b >= 0:
            # a is negative
            pass
        else:
            a2 = self.getSumOfUnsigned(~a, 1)
            b2 = self.getSumOfUnsigned(~b, 1)
            r = self.getSumOfUnsigned(a2, b2)
            return -r
