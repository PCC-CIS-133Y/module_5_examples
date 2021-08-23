# example 5.28
def make_reuben():
    # let's change the cheese
    return ("corned beef", "swiss cheese", "sauerkraut", "russian dressing", "rye bread")

# or we can loop through with a for loop

print("Reuben ingredients:")

for item in make_reuben():
    print(item)