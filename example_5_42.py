# example 5.42
prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

for price in prices.values():
    print("${:,.2f}".format(price))

