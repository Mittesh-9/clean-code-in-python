# Generators
# A generator is a function in Python which returns an iterator object instead of one single value. The main difference between normal functions and generators is that generators use the yield keyword instead of return. Each next value in the iterator is fetched using next(generator).

# Let's say we want to generate the first n multiples of x. Our generator would look something like this:

def multiple_generator(x, n):
    for i in range(1, n + 1):
        yield x * i

multiples_of_5 = multiple_generator(5, 3)

print(next(multiples_of_5))  # 5
print(next(multiples_of_5))  # 10
print(next(multiples_of_5))  # 15
