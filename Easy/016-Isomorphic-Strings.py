# DATE: 29/10/2026
#
# PROBLEM LINK:https://leetcode.com/problems/isomorphic-strings/description/
# PROBLEM STATEMENT: Isomorphic Strings
# DIFFICULTY: Easy
# __________________________________________________
# 
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.


# Example 2:
# Input: s = "f11", t = "b23"
# Output: false
# Explanation:
# The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

 

# Constraints:
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
 

# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# - Isomorphic strings require a one-to-one mapping.
# - Use TWO hash maps to maintain mapping in both directions: s → t and t → s.
# - Check an existing mapping before updating it.
# - If either direction conflicts, return False.
# - Think: "same character → same character" AND "different characters → different characters".
# - Time: O(n), Space: O(k).
# __________________________________________________


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in s_to_t and s_to_t[a] != b:
                return False

            if b in t_to_s and t_to_s[b] != a:
                return False

            s_to_t[a] = b
            t_to_s[b] = a

        return True