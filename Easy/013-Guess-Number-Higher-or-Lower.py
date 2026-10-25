# DATE: 24/10/2026
#
# PROBLEM LINK:
# PROBLEM STATEMENT: Guess Number HIgher or Lower
# DIFFICULTY: Easy
# __________________________________________________
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
#
#
#
# Example 1:
# Input: n = 10, pick = 6
# Output: 6
#
# Example 2:
# Input: n = 1, pick = 1
# Output: 1
# Example 3:
#
# Input: n = 2, pick = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n
#
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# - Ye pure binary search hai, bas comparison array ke bajay guess() API se hota hai.
# - guess() ka sign ulta lag sakta hai: -1 matlab MERA guess bada hai (high = mid - 1),
#   +1 matlab MERA guess chhota hai (low = mid + 1). Yahan confusion hota hai!
# - mid = low + (high - low) // 2 -> overflow-safe formula (C++/Java mein zaroori).
# - Loop condition low <= high, kyunki ek element bachne par bhi check karna hai.
# - Time: O(log n), Space: O(1)
# __________________________________________________

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = low + (high - low) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result < 0:
                high = mid - 1
            else:
                low = mid + 1