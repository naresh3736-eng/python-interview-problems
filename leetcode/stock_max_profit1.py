"""
input: given a list of stock prices [10,13,3,10]
Output: max profit should be 7 becasue buying at 3 and selling at 10 is giving max profit
"""
def maxProfit(prices):
    # profit = 0
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit = prices[i] - prices[i-1]
            max_profit = max(max_profit, profit)
    return max_profit

prices = [10,13,3,10]

print(maxProfit(prices))

