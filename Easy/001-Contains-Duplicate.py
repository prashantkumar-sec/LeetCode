# DATE: 11/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/contains-duplicate/description/
# PROBLEM STATEMENT: Contains Duplicate
# DIFFICULTY: Easy
#  __________________________________________________
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

 

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# - Brute force is O(n^2), which gives TLE when n = 10^5
# - When a problem asks "have I seen this before?" or "is there a duplicate?", think Hash Set (O(1) average lookup)
# - `in` checks membership in a collection; `is` checks whether two names point to the same object (use `in` here)
# - Trade-off: Set = O(n) time, O(n) space | Sorting = O(n log n) time, O(1) extra space
# - Pattern: same "seen before" family as Two Sum
#
# TIME: O(n)   SPACE: O(n)
# __________________________________________________

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

