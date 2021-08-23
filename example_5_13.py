# example 5.13
# just for fun, let's try the "for" loop with our sandwich list
sandwiches = ["chipotle chicken", "reuben", "ham and cheese", "meatball"]

menu = ""
for sandwich in sandwiches:
    menu += sandwich + ", "
print(menu)