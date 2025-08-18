# https://neetcode.io/problems/missing-number?list=neetcode150


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor1 = 0
        max_num = -1
        for num in nums:
            xor1 ^= num
            if num > max_num:
                max_num = num

        xor2 = 0
        for n in range(max_num + 1):
            xor2 ^= n

        return xor1 ^ xor2 if max_num != len(nums) - 1 else max_num + 1
