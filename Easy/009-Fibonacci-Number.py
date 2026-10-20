# DATE: 20/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/fibonacci-number/
# PROBLEM STATEMENT: Fibonacci Number
# DIFFICULTY: Easy
# __________________________________________________
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n). 
#
# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
# Constraints:
# 0 <= n <= 30
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Fibonacci follows:
#    F(n) = F(n-1) + F(n-2)
#
# 2. Base cases:
#    F(0) = 0
#    F(1) = 1
#
# 3. We only need the previous two values to calculate the next value.
#
# 4. No array is required. We can solve it using two variables.
#
# 5. `a` stores the current Fibonacci number.
#    `b` stores the next Fibonacci number.
#
# 6. Python tuple assignment:
#    a, b = b, a + b
#    updates both variables simultaneously.
#
# 7. After n iterations, `a` contains F(n).
#
# 8. Iterative solution is better than simple recursion because
#    recursion repeats the same calculations many times.
#
# 9. Time Complexity: O(n)
#    Space Complexity: O(1)
#
# 10. QUICK REVISION:
#     If a problem depends only on the previous few values,
#     check whether an array can be replaced with a few variables.
#
# PATTERN:
# # Previous two values are enough → Use two variables instead of an array.
# __________________________________________________


class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1

        for i in range(n):
            a, b = b ,a+b

        return a