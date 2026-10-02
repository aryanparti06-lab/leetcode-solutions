# LeetCode 283: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Topic: Array, Two Pointers
# Approach: Two pointers. 'right' scans the array; whenever it finds a
#           non-zero, swap it with the 'left' position and move 'left' forward.
#           This keeps non-zeros in order and pushes zeroes to the end.
# Time: O(n), Space: O(1)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
