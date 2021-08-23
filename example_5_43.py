# example 5.43
# let's keep our dictionary of sandwich prices, but move them out of order

prices = {"meatball": 13, "chipotle chicken": 10, "ham and cheese": 12, "reuben": 11}

# here we are creating a list called sandwich_prices
sandwich_prices = list(prices.values())

# to check on our list, let's print it out
print(sandwich_prices)

# now that our list is created, we use the sort() method
sandwich_prices.sort()

# now let's see if our sandwich prices are sorted in order
for price in sandwich_prices:
    print("${:,.2f}".format(price))

