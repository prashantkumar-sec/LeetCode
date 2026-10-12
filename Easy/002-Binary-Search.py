# DATE: 12/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/binary-search/description/
# PROBLEM STATEMENT: Binary Search
# DIFFICULTY: Easy
# __________________________________________________
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 
# Constraints:
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Binary Search works only when the array is sorted.
#
# 2. Instead of checking every element, check the middle element.
#
# 3. If nums[mid] == target:
#       → Target found → return mid
#
# 4. If nums[mid] > target:
#       → Target must be on the left side
#       → high = mid - 1
#
# 5. If nums[mid] < target:
#       → Target must be on the right side
#       → low = mid + 1
#
# 6. The search space is reduced by roughly half after every iteration.
#
# 7. Important condition:
#       while low <= high
#
# 8. Safe/common way to calculate middle:
#       mid = low + (high - low) // 2
#
# 9. If low > high:
#       → Search space is empty
#       → Target doesn't exist → return -1
#
# COMPLEXITY:
# Time  : O(log n)
# Space : O(1)
#
# QUICK REVISION:
# "Sorted array + search → think Binary Search."
# "Compare middle → eliminate half → repeat."
#
# __________________________________________________

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1