'''
input: given a list of stock prices [10,13,3,10]
Output: max profit should be 7 becasue buying at 3 and selling at 10 is giving max profit
'''

def maximum_profit(stock_list):
    min_stock_price = stock_list[0]

    max_profit = stock_list[1] - stock_list[0]

    for price in stock_list[1:]:
        comparison_profit = price - min_stock_price

        max_profit = max(max_profit, comparison_profit)

        min_stock_price = min(price, min_stock_price)

    return max_profit

alist = [7,1,5,3,6,4]
print(maximum_profit(alist))

def maxinum_profit2(stock_list):
    profit = 0
    max_profit = 0
    for i in range(1, len(stock_list)):
        if stock_list[i] > stock_list[i-1]:
            profit += stock_list[i] - stock_list[i-1]
            max_profit = max(max_profit, profit)
    return profit

alist1 = [7,1,5,3,6,4]
print(maxinum_profit2(alist))

