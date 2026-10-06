# LeetCode 11: Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Topic: Array, Two Pointers, Greedy
# Approach: Start with pointers at both ends. The area is limited by the
#           shorter line, so move the pointer at the shorter line inward
#           in the hope of finding a taller one. Track the max area seen.
# Time: O(n), Space: O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            heights = min(height[left], height[right])
            area = heights * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
