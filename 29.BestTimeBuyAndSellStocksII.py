class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize profit variable to keep track of total profit
        profit = 0
        # Iterate through the prices array
        for i in range(len(prices) - 1):
            # Check if the price on the next day is greater than the price on the current day
            if prices[i + 1] > prices[i]:
                # If so, calculate the profit by selling the stock on the next day and buying it on the current day
                profit += prices[i + 1] - prices[i]
        # Return the total profit achieved
        return profit
