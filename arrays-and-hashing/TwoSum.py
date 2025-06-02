# https://neetcode.io/problems/two-integer-sum?list=neetcode150


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                hashmap[difference]
                return sorted([i, hashmap[difference]])
            hashmap[num] = i
        return [-1, -1]
