# LeetCode 345: Reverse Vowels of a String
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Topic: String, Two Pointers
# Approach: Convert the string to a list. Move 'left' forward and 'right'
#           backward until each points at a vowel, then swap them and
#           continue until the pointers meet.
# Time: O(n), Space: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] not in "aeiouAEIOU":
                left += 1
                continue
            if s[right] not in "aeiouAEIOU":
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
