def buy_sell(prices:list[int])->int:
    minimum_price=prices[0]
    max_profit=0
    for i in range(1,len(prices),1):
        if prices[i]<minimum_price:
            minimum_price=prices[i]
        else:
            profit=prices[i]-minimum_price
            max_profit=max(profit,max_profit)
    return max_profit

def stock_prices():
    days=int(input("enter the days of the stock histery: "))
    prices=[]
    for i in range(0,days,1):
        price=int(input(f"enter {i+1} days of the prices: "))
        prices.append(price)
    
    ans=buy_sell(prices)
    print(f'the maximum profit is {ans}')
    
stock_prices()