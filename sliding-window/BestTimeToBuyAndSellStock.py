# https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_cp = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < lowest_cp:
                lowest_cp = prices[i - 1]
            profit = prices[i] - lowest_cp
            if profit > max_profit:
                max_profit = profit
        return max_profit
