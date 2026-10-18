# DATE: 18/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/valid-palindrome/
# PROBLEM STATEMENT: Valid Palindrome
# DIFFICULTY: Easy
# __________________________________________________
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# - A palindrome can be checked efficiently using the Two Pointer technique.
# - Use one pointer from the beginning and one from the end.
# - Skip non-alphanumeric characters using isalnum().
# - Compare characters after converting them to lowercase.
# - If any pair of characters differs, return False immediately.
# - If the pointers cross without finding a mismatch, return True.
# - Two-pointer approach avoids creating an additional cleaned string.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
# - Important pattern: Two Pointers + String Processing.
# __________________________________________________


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned =""
        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()
        return cleaned == cleaned[::-1]
