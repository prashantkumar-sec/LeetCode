# DATE: 15/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/number-of-good-pairs/
# PROBLEM STATEMENT: Number of Good Pairs
# DIFFICULTY: Easy
# __________________________________________________
# Given an array of integers nums, return the number of good pairs. A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
#
# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
#
# Example 3:
# Input: nums = [1,2,3]
# Output: 0
# 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 1. To generate unique index pairs where i < j, use: for j in range(i + 1, len(nums))
# 2. If nums[i] == nums[j], increment the pair count.
# 3. Brute-force pair checking is O(n²) and is acceptable when n is small.
# 4. Important pattern: "Count pairs satisfying a condition" → nested loops are often the simplest approach.
# __________________________________________________


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count += 1
                
        return count