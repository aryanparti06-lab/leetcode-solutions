# LeetCode 344: Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# Topic: String, Two Pointers
# Approach: Use Python's built-in list.reverse(), which reverses the
#           list in place.
# Time: O(n), Space: O(1)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        return s.reverse()
