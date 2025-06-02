# https://neetcode.io/problems/two-integer-sum?list=neetcode150


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {num: index for index, num in enumerate(nums)}
        for i, num in enumerate(nums):
            num2 = target - num
            j = indices_map.get(num2)
            if j is not None and i != j:
                return [i, j]
        return [-1, -1]
