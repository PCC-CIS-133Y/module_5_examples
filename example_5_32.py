# example 5.32
prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

# get() method to check the dictionary for a key

sandwich = prices.get("reuben")

if sandwich:
    print(sandwich)
else:
    print("There is no sandwich by that name")
