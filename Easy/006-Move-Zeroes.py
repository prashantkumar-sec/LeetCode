# DATE: 16/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/move-zeroes/description/
# PROBLEM STATEMENT: Move Zeroes
# DIFFICULTY: Easy
# __________________________________________________
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Brute force: remove each 0 and append it to the end. Works, but list.remove() is O(n)
#    per call, so total time is O(n^2).
# 2. Modifying a list while iterating over it is risky (elements shift under the iterator).
#    It happens to work here because appended zeros are revisited, but it is not a safe habit.
# 3. Optimal approach: Two Pointers (read/write). Write pointer = where the next non-zero goes,
#    read pointer scans the array. Swap non-zeros forward -> O(n) time, O(1) space, one pass.
# 4. Same pattern appears in: Remove Element, Remove Duplicates from Sorted Array.
# ____________________


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        