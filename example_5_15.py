# example 5.15
sandwiches = ["chipotle chicken", "reuben", "ham and cheese", "meatball"]
prices = [10, 11, 12, 13]

# we can create a function that will change the data in both lists

def add_to_list(list, item):
    list.append(item)

add_to_list(sandwiches, "monte cristo")
add_to_list(prices, 14)

print(sandwiches)
print(prices) 