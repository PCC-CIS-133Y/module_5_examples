# example 5.27
# you can also use tuples with functions

def make_reuben():
    return ("corned beef", "swiss cheese", "sauerkraut", "russian dressing", "rye bread")

# we can unpack this list and assign each of these to a variable
meat, cheese, topping, dressing, bread = make_reuben()

print("reuben sandwich is made of ", meat, cheese, topping, dressing, bread )