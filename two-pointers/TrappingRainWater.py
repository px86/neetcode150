# https://neetcode.io/problems/trapping-rain-water?list=neetcode150


class Solution:
    def trap(self, height: List[int]) -> int:
        lhs = [0] * len(height)
        rhs = [0] * len(height)

        for i in range(1, len(height)):
            lhs[i] = max(lhs[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            rhs[i] = max(rhs[i + 1], height[i + 1])

        water_trapped = 0

        for i in range(len(height)):
            water_trapped_at_point = min(lhs[i], rhs[i]) - height[i]
            if water_trapped_at_point > 0:
                water_trapped += water_trapped_at_point

        return water_trapped
