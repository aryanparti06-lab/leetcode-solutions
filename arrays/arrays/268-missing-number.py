# LeetCode 268: Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Topic: Array, Math
# Approach: Check every number from 0 to n and return the one not in nums
# Time: O(n^2), Space: O(1)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(1 + len(nums)):
            if i not in nums:
                return i
