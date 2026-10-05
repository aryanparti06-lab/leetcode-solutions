# LeetCode 125: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Topic: String, Two Pointers
# Approach: Lowercase the string, then use two pointers from both ends.
#           Skip any non-alphanumeric characters, and return False as soon
#           as two compared characters differ.
# Time: O(n), Space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
