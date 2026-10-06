# LeetCode 1: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Topic: Array, Hash Table
# Approach: Brute force. Check every pair (i, j) with j > i and return
#           the indices of the pair whose sum equals the target.
# Time: O(n^2), Space: O(1)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
