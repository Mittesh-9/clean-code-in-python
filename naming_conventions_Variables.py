# Naming Conventions
# One of the most important aspects of writing clean code is naming conventions. You should always use meaningful and intention-revealing names. It's always better to use long, descriptive names than short names with comments.

# This is bad
# represents the number of active users
au = 55

# This is good
active_user_amount = 55
We'll look at more examples in the next two sections.


# Variables >>
# 1. Use nouns for variable names

# 2. Use descriptive/intention-revealing names
# Other developers should be able to figure out what a variable stores just by reading its name.

# This is bad
c = 5
d = 12

# This is good
city_counter = 5
elapsed_time_in_days = 12

# 3. Use pronounceable names
# You should always use pronounceable names; otherwise, you'll have a hard time explaining your algorithms out loud.

from datetime import datetime

# This is bad
genyyyymmddhhmmss = datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')

# This is good
generation_datetime = datetime.strptime('04/27/95 07:14:22', '%m/%d/%y %H:%M:%S')

# 4. Avoid using ambiguous abbreviations
# Don't try to come up with your own abbreviations. It's better for a variable to have a longer name than a confusing name.

# This is bad
fna = 'Bob'
cre_tmstp = 1621535852

# This is good
first_name = 'Bob'
creation_timestamp = 1621535852

# 5. Always use the same vocabulary
# Avoid using synonyms when naming variables.

# This is bad
client_first_name = 'Bob'
customer_last_name = 'Smith'

# This is good
client_first_name = 'Bob'
client_last_name = 'Smith'

# 6. Don't use "magic numbers"
# Magic numbers are strange numbers that appear in code, which do not have a clear meaning. Let's take a look at an example:

import random

# This is bad
def roll():
    return random.randint(0, 36)  # what is 36 supposed to represent?

# This is good
ROULETTE_POCKET_COUNT = 36

def roll():
    return random.randint(0, ROULETTE_POCKET_COUNT)
# Instead of using magic numbers, we can extract them into a meaningful variable.

# 7. Use solution domain names
# If you use a lot of different data types in your algorithm or class and you can't figure them out from the variable name itself, don't be afraid to add data type suffix to your variable name. For example:

# This is good
score_list = [12, 33, 14, 24]
word_dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cherry',
}
# And here's a bad example (because you can't figure out the data type from the variable name):

# This is bad
names = ["Nick", "Mike", "John"]
8. Don't add redundant context
# Do not add unnecessary data to variable names, especially if you're working with classes.

# This is bad
class Person:
    def __init__(self, person_first_name, person_last_name, person_age):
        self.person_first_name = person_first_name
        self.person_last_name = person_last_name
        self.person_age = person_age


# This is good
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
# We're already inside the Person class, so there's no need to add a person_ prefix to every class variable.
