class Solution:
    def maxProfit(self, prices: list[int]) -> int:
       profit =0
       minm = (float) ("inf")
       n = len(prices)
       for i in range (0,n):
        minm = min(minm,prices[i])
        profit = max(profit,prices[i]-minm)
       return profit 