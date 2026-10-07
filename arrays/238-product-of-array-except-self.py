# LeetCode 238: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Topic: Array, Prefix Sum
# Approach: Two passes without division. First pass stores the product of
#           everything to the left of each index in 'answer'. Second pass
#           walks backward and multiplies in the product of everything to
#           the right using a running 'suffix'.
# Time: O(n), Space: O(1) extra (the output array doesn't count)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
