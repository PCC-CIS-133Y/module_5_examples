# example 5.39
# here is our beginning dictionary of sandwich prices

prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

for price in prices.keys():
    print(price + "  " + str(prices[price]))

