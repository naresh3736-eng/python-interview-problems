def countStockSymbols(picks):
    lookup = {}
    user_set = set()

    for item in picks:
        lst = item.split(',')
        user_id, stock_symbol = lst[0], lst[1]
        # print(user_id, stock_symbol)
        if stock_symbol in lookup and user_id not in user_set:
            lookup[stock_symbol] += 1
        else:
            if user_id in user_set:
                continue
            lookup[stock_symbol] = 1
            user_set.add(user_id)
    return sorted(lookup.items(), key=lambda item: item[1], reverse=True)

print(countStockSymbols(["1,AAPL", "2,GOOGL", "1,FB", "3,FB", "4,GOOGL"]))
# output: ['AAPL,1', 'GOOGL,2', 'FB,1']