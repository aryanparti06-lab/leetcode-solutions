# LeetCode 121: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Topic: Array, Dynamic Programming
# Approach: Single pass. Track the lowest price seen so far as the best
#           day to buy. At each price, compute the profit if sold today
#           and keep the maximum.
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
