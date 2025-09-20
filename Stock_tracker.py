# Stock Portfolio Tracker

# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

# Step 2: User input with validation
portfolio = {}
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        while True:
            qty_input = input(f"Enter quantity of {stock}: ")
            if qty_input.isdigit():
                qty = int(qty_input)
                break
            else:
                print("❌ Please enter a valid number.")
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("❌ Stock not found in dictionary.")

# Step 3: Calculate total investment
total_value = 0
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × {price} = {value}")

print(f"\n💰 Total Investment Value = {total_value}")

# Step 4: Save portfolio to a text file (UTF-8 encoding)
with open("portfolio.txt", "w", encoding="utf-8") as file:
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        file.write(f"{stock}: {qty} × {price} = {value}\n")
    file.write(f"\nTotal Investment Value = {total_value}")

print("\n✅ Portfolio saved to portfolio.txt")
