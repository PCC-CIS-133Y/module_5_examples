# example 5.9
sandwiches = ["chipotle chicken", "reuben", "ham and cheese", "meatball"]

# we want to remove the "meatball" sandwich but it's best to check for it 
# first so we don't get an error
item = "salami"
if item in sandwiches:
    sandwiches.remove(item)
print(sandwiches)