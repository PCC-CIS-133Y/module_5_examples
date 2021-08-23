# example 5.38
prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

# you can also use pop() with an if statement to avoid a KeyError

sandwich = "chicken salad"

if sandwich in prices:
    prices.pop(sandwich)
    print(prices)
else:
    print("There is no sandwich by that name")