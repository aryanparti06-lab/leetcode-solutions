# Maximum Sum Subarray of Size K (similar to LeetCode 643)
# Related: https://leetcode.com/problems/maximum-average-subarray-i/
# Topic: Array, Sliding Window
# Approach: Compute the sum of the first k elements. Then slide the window
#           one step at a time: subtract the element leaving the window
#           and add the element entering it. Track the maximum sum seen.
# Time: O(n), Space: O(1)

class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        window_sum = 0
        for r in range(k):
            window_sum += nums[r]
        max_sum = window_sum
        for r in range(k, len(nums)):
            window_sum = window_sum - nums[r - k] + nums[r]
            max_sum = max(max_sum, window_sum)
        return max_sum
