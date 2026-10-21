# DATE: 21/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/add-digits/description/
# PROBLEM STATEMENT: Add Digits
# DIFFICULTY: Easy
# __________________________________________________
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
#
#
#
# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
#
# Example 2:
# Input: num = 0
# Output: 0
#
#
# Constraints:
#
# 0 <= num <= 231 - 1
#
#
# Follow up: Could you do it without any loop/recursion in O(1) runtime?
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# This problem is a Digital Root problem.
# straightforward approach: repeatedly calculate the sum of digits until only one digit remains.
# num % 10 → gives the last digit.
# num // 10 → removes the last digit.
# Straightforward solution: O(log n) time, O(1) space.
# Follow-up asks for O(1) without loop/recursion.
# Key mathematical trick: repeated digit sum is the digital root.
# For num > 0, the answer can be found using modulo 9.
# Formula: 1 + (num - 1) % 9
# Special case: num = 0 → answer is 0.
# Quick pattern to remember: Repeated digit sum → Digital Root → Modulo 9
# __________________________________________________

class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            total = 0

            while num > 0:
                    digit = num%10
                    total = total+digit
                    num = num//10
            num = total
        return num
