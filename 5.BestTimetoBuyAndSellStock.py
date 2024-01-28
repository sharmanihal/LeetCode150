
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the smallest price to the left and the maximum profit
        min_price = prices[0]
        max_profit = 0
        
        # Iterate through the prices starting from the second day
        for current_price in prices[1:]:
            # Calculate the potential profit for the current day and update max_profit if needed
            max_profit = max(max_profit, current_price - min_price)
            
            # Update the minimum price if the current price is smaller
            min_price = min(min_price, current_price)
        
        # Return the maximum profit achieved from the transaction
        return max_profit
"""
Explanation:

1. The code uses two variables, `min_price` and `max_profit`, to keep track of the smallest price to the left and the maximum profit, respectively.

2. The loop starts from the second day (`prices[1:]`) because you need at least two days to make a valid transaction (buy and sell).

3. For each day, it calculates the potential profit by subtracting the `min_price` from the current day's price (`current_price - min_price`). If this potential profit is greater than the current `max_profit`, it updates `max_profit` with the new value.

4. The `min_price` is updated to the minimum of its current value and the current day's price. This is done to keep track of the smallest price encountered so far.

5. The loop continues through the entire array of prices.

6. Finally, the function returns the maximum profit achieved from the transaction.

The key idea is to iterate through the prices while keeping track of the minimum price encountered. At each step, the potential profit is calculated, and if it's greater than the current maximum profit, the maximum profit is updated.
"""
