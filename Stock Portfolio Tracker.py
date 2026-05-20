stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 320
}

total = 0
records = []

print("Stock Portfolio Tracker")

while True:

    stock = input("\nEnter stock name: ").upper()

    if stock not in stocks:
        print("Stock not found")
        continue

    qty = int(input("Enter quantity: "))

    price = stocks[stock]
    cost = price * qty

    total += cost

    records.append((stock, qty, cost))

    print("Added:", stock, "x", qty)
    print("Cost:", cost)

    more = input("Add more? (yes/no): ").lower()

    if more != "yes":
        break

print("\n----- Summary -----")

for r in records:
    print(r[0], "x", r[1], "=", r[2])

print("\nTotal Investment:", total)

# save to file
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Summary\n\n")

for r in records:
    file.write(r[0] + " x " + str(r[1]) + " = " + str(r[2]) + "\n")

file.write("\nTotal Investment = " + str(total))

file.close()

print("Saved to portfolio.txt")