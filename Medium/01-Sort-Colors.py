# DATE: 17/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/sort-colors/
# PROBLEM STATEMENT: Sort Colors
# DIFFICULTY: Medium
# __________________________________________________
# You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Explanation:
# The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Explanation:
# The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.
#
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Since the array contains only 0, 1, and 2, we don't need a
#    general sorting algorithm.
#
# 2. Count the frequency of each value and then overwrite the array.
#
# 3. This is a Counting Sort idea for a very small fixed range.
#
# 4. Time Complexity: O(n)
#    Space Complexity: O(1)
#
# 5. Important: nums must be modified in-place, so we rewrite the
#    original array instead of creating a new sorted array.
#
# 6. Another optimal solution is the Dutch National Flag algorithm,
#    which sorts the array in one pass using three pointers:
#    low, mid, high.
#
# QUICK REVISION:
# Count 0, 1, 2 -> rewrite nums.
# Alternative: 3 pointers -> 0 | 1 | unknown | 2
# __________________________________________________


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = [0,0,0]

        for num in nums:
            count[num] += 1
        
        i =0
        for j in range(3):
            for _ in range(count[j]):
                nums[i] = j
                i += 1