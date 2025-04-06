class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        bought_index = 0
        max_profit = 0

        for sold_index in range(1, len(prices)):
            if prices[sold_index] > prices[bought_index]:
                max_profit = max(max_profit, prices[sold_index] - prices[bought_index])
            else:
                bought_index = sold_index
            
        return max_profit

        