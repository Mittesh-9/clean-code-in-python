# Context Managers
# Context managers simplify how we interact with external resources, like files and databases. The most common usage is the with statement. The good thing about them is that they automatically deallocate memory outside of their block.

# Let's look at an example:

with open('wisdom.txt', 'w') as opened_file:
    opened_file.write('Python is cool.')

# opened_file has been closed.
# Without a context manager our code would look like this:

file = open('wisdom.txt', 'w')
try:
    file.write('Python is cool.')
finally:
    file.close()
