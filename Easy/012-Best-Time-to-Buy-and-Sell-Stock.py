# DATE: 23/10/2026
#
# PROBLEM LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# PROBLEM STATEMENT: Best Time to Buy and Sell Stock
# DIFFICULTY: Easy
# __________________________________________________
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# - Brute force (har buy-sell pair check karna) O(n^2) hai, n = 10^5 pe TLE aayega.
# - Trick: ek hi pass mein "ab tak ka minimum" track karo, aur har din
#   check karo ki aaj bechne pe kitna profit hota.
# - Min hamesha current day se pehle ya usi din ka hota hai, so "buy before sell"
#   automatically handle ho jaata hai.
# - max_profit = 0 se start karo, taaki jab price sirf gir rahi ho to answer 0 aaye.
# - Pattern: running min / running max / prefix tracking, ye Kadane's
#   algorithm jaisa hi "carry forward state" wala idea hai.
# - Time: O(n), Space: O(1)
# __________________________________________________


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest = prices[0]
        max_profit = 0

        for price in prices:
            if price < cheapest:
                cheapest = price

            profit = price - cheapest

            if profit > max_profit:
                max_profit = profit

        return max_profit
