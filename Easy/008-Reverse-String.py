# DATE: 19/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/reverse-string/description/
# PROBLEM STATEMENT: Reverse String
# DIFFICULTY: Easy
# __________________________________________________
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character. 


class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Two Pointer Technique:
#    Use one pointer from the beginning (left) and one from the end (right).
#
# 2. In-place modification:
#    Modify the original array instead of creating a new array.
#
# 3. Swapping:
#    Python allows swapping without a temporary variable:
#    s[left], s[right] = s[right], s[left]
#
# 4. Loop condition:
#    while left < right
#    We stop when the pointers meet or cross.
#
# 5. Time Complexity:
#    O(n)
#    Each element is processed at most once.
#
# 6. Space Complexity:
#    O(1)
#    Only two pointer variables are used.
#
# 7. Important pattern:
#    Two pointers are useful when working from both ends of an array/string.
# __________________________________________________
