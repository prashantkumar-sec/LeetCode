# DATE: 28/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/valid-anagram/description/
# PROBLEM STATEMENT: Valid Anagram
# DIFFICULTY: Easy
# __________________________________________________
# 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# - Anagram = same characters with same frequencies. Pehle length check karo (quick reject).
# - Frequency count: s se +1, t se -1. Agar kabhi count < 0 ho gaya ya char hi nahi mila → False.
# - Length equal hai, to koi count negative nahi gaya matlab sab zero hain, extra check ki zaroorat nahi.
# - Shortcut: collections.Counter(s) == Counter(t)  ya  sorted(s) == sorted(t) (O(n log n)).
# - Lowercase only hai to fixed array [0]*26 use kar sakte ho (index = ord(c) - ord('a')), dict se thoda fast.
# - Follow-up (Unicode): dict/Counter hi use karo, array 26 ka fix nahi chalega. Python 3 ke str already Unicode code points handle karta hai.
#   Agar combining characters ho (e.g. "é" ka alag forms), to pehle unicodedata.normalize("NFC", s) karo, phir count karo.
# - Time: O(n), Space: O(k), k = distinct chars (lowercase me max 26 to effectively O(1)).
# __________________________________________________


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        
        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False
        return True