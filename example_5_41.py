# example 5.41
prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

for sandwich, price in prices.items():
    print(sandwich + " sandwich costs " + "${:,.2f}".format(price))
    
# notice how I formatted the price to currency to add some context to our dictionary output

