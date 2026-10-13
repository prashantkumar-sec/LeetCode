# DATE: 13/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/palindrome-number/
# PROBLEM STATEMENT: Palindrome Number
# DIFFICULTY: Easy
# __________________________________________________
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Constraints:
# -231 <= x <= 231 - 1
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. A palindrome reads the same from both directions.
#
# 2. Simple approach:
#    Convert integer → string
#    Reverse string using [::-1]
#    Compare original and reversed string.
#
# 3. Negative numbers are automatically not palindromes.
#    Example: -121 → "121-" after reversal.
#
# 4. Numbers ending in 0 cannot be palindromes unless the number is 0.
#    Example: 10 → 01 → false
#
# 5. Python trick:
#    s[::-1] reverses a string.
#
# 6. Follow-up:
#    Can we solve it without converting the integer to a string?
#    → Yes, by reversing the digits mathematically.
#
# COMPLEXITY OF MY SOLUTION:
# Time  : O(d)
# Space : O(d)
# where d = number of digits.
#
# QUICK REVISION:
# "Palindrome → original == reversed"
#
# __________________________________________________

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)[::-1]
        x1 = str(x) 
        if x1 == num:
            return True
        return False