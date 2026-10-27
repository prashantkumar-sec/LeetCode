# DATE: 27/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/two-sum/
# PROBLEM STATEMENT:  Two Sum
# DIFFICULTY: Easy
# __________________________________________________
#
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation:
# The sum of nums[0] and nums[1] is 2 + 7 = 9, which equals the target. Therefore, the indices [0, 1] are returned.

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Explanation:
# The sum of nums[1] and nums[2] is 2 + 4 = 6, which equals the target. Therefore, the indices [1, 2] are returned.

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
# Explanation:
# The sum of nums[0] and nums[1] is 3 + 3 = 6, which equals the target. Therefore, the indices [0, 1] are returned.


# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Brute force is O(n^2), checking every pair. A hash map brings it to O(n) via lookups.
# 2. Trick: instead of searching for a number, search for its complement = target - num.
# 3. Check first, then store -> the same element is never reused,
#    and duplicates like [3,3] are handled correctly.
# 4. Pattern: "pair/complement with a given sum" => hash map (seen) in one pass.
#    If the array is sorted, two pointers also work, but when indices are needed
#    the hash map is the best choice.
# 5. Time: O(n), Space: O(n)
# __________________________________________________


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        return []
                