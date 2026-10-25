# LeetCode 438: Find All Anagrams in a String
# Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Topic: String, Hash Table, Sliding Window
# Approach: For every window of length len(p) in s, build a Counter of
#           the window and compare it with the Counter of p. If equal,
#           the window start index is an anagram start.
# Time: O(n * k), Space: O(k)  (n = len(s), k = len(p))

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_count = Counter(p)
        k = len(p)
        ans = []
        for r in range(len(s) - k + 1):
            window = s[r:r+k]
            window_count = Counter(window)
            if window_count == p_count:
                ans.append(r)
        return ans
