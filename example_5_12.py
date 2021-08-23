# example 5.12
prices = [10, 11, 12, 13]

# let's try this one more time with a "while" loop

total = 0
i = 0
while i < len(prices):
    total += prices[i]
    i += 1
print(total)