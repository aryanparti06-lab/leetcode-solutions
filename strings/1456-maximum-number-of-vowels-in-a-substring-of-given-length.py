# LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length
# Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Topic: String, Sliding Window
# Approach: Count the vowels in the first k characters. Slide the window
#           one step at a time: subtract 1 if the character leaving is a
#           vowel, add 1 if the character entering is a vowel. Track the
#           maximum count seen.
# Time: O(n), Space: O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        window_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                window_vowels += 1
        max_vowels = window_vowels
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                window_vowels -= 1
            if s[i] in vowels:
                window_vowels += 1
            max_vowels = max(max_vowels, window_vowels)
        return max_vowels
