# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

#we always want to buy low and sell high
#TWO POINTERS
#profitable means prices[r] > prices[l]
#profit is the difference
#initialize max profit = 0
#we want to keep updating profit so long as new profit we get > cur profit
#iterate while r is < len(prices) - does not go out of bounds


#        SOLUTION1
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         l, r = 0, 1 #l= buy, r= sell
#         MaxProfit =  0
#         while r < len(prices):
#         #is it profitable?
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 MaxProfit = max(MaxProfit, profit)
#             else: #shift l all the way to r is would be the cur lowest price
#                 l =r
#             r +=1 #either way move r forward
#         return MaxProfit
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
#     print(solution.maxProfit([7, 6, 4, 3, 1]))       # Output: 0


#       SOLUTION2

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf') #initialize to a very large number
        max_P = 0 #start with no profit
        for price in prices:
            if price < min_price:
                min_price = price # update min_price if we found a lower price
            profit = price - min_price #calculate profit if we sel at cur price
            max_P = max(max_P, profit) # update max profit if we find a higher profit
        return max_P 
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print(solution.maxProfit([7, 6, 4, 3, 1]))       # Output: 0




