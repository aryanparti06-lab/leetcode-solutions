# LeetCode 643: Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Topic: Array, Sliding Window
# Approach: Compute the sum of the first k elements. Slide the window one
#           step at a time by subtracting the element leaving and adding
#           the element entering. Track the maximum sum, then divide by k
#           once at the end.
# Time: O(n), Space: O(1)

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        return max_sum / k
