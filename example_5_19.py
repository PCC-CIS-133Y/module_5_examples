# example 5.19
menu = [["chipotle chicken", 10],
        ["reuben", 11],
        ["ham and cheese", 12],
        ["meatball", 13],
        ["monte cristo", 14],
        ["roast beef", 15]]


# so now let's make that menu look nice in our console using a loop

for menuitem in menu:
    for item in menuitem:
        print(item, end=" |")
    print()