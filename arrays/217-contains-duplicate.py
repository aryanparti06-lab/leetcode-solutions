# LeetCode 217: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Topic: Array, Hash Set
# Approach: Store seen numbers in a set; if a number repeats, return True
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
