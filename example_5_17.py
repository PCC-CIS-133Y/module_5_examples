# example 5.17
# let's write a function to double the price of our sandwiches
def double_the_price(price):
    price = price * 2
    return price

# now we can use this to demonstrate an immutable data type

price1 = 10
price2 = double_the_price(price1)
print(price1)
print(price2)

# In this case you cannot have both prices in one object,
# so you need a new object to be assigned the value of the second price. 