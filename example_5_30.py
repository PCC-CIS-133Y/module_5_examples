# example 5.30
prices = {"chipotle chicken": 10, "reuben": 11, "ham and cheese": 12, "meatball": 13}

# get an item from our dictionary

print("${:,.2f}".format(prices["reuben"]))

# notice how I've added in the Python code to format this price as currency in the output

# you can also start to add some context

print("A reuben costs " + "${:,.2f}".format(prices["reuben"]))
