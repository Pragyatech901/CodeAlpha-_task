stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 150,
    "MSFT": 420
}

total_investment = 0

print("Available Stocks:", ", ".join(stock_prices.keys()))

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(stock, "Investment =", investment)
    else:
        print("Stock not available!")

print("Total Investment =", total_investment)
