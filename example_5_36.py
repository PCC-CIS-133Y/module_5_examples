# example 5.36
prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

# now let's use a loop to check and see if a sandwich exists in our dictionary  
# before we delete it

sandwich = "chicken salad"

if sandwich in prices:
    price = prices[sandwich]
    del prices[sandwich]
    print(prices)
else:
    print("There is no sandwich by that name")
