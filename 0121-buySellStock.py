class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowestPrice = float('inf')
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
            else:
                profit = prices[i] - lowestPrice
                maxProfit = max(profit, maxProfit)
        return maxProfit

