# Iterators
# An iterator is an object that contains a countable number of values. Iterators allow an object to be iterated upon, which means that you can traverse through all the values.

# Let's say we have a list of names and we want to loop through it. We can loop through it using next(names):

names = ["Mike", "John", "Steve"]
names_iterator = iter(names)

for i in range(len(names)):
    print(next(names_iterator))

# Or use an enhanced loop:

names = ["Mike", "John", "Steve"]

for name in names:
    print(name)
  
# Inside of enhanced loops avoid using variable names like item or value because it makes it way harder to tell what a variable stores, especially in nested enhanced loops.
