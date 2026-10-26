# LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
# Topic: Array, Sliding Window
# Approach: Compute the sum of the first k elements. Slide the window one
#           step at a time (subtract the leaving element, add the entering
#           one). Instead of computing averages, compare the window sum
#           with k * threshold, which avoids division and float issues.
#           Count every window that meets the condition.
# Time: O(n), Space: O(1)

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = 0
        count = 0
        for i in range(k):
            window_sum += arr[i]
        if window_sum >= k * threshold:
            count += 1
        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]
            if window_sum >= k * threshold:
                count += 1
        return count
