# Functions
# 1. Use verbs for function names
# 2. Do not use different words for the same concept
# Pick a word for each concept and stick to it. Using different words for the same concept will cause confusion.

# This is bad
def get_name(): pass
def fetch_age(): pass

# This is good
def get_name(): pass
def get_age(): pass
  
# 3. Write short and simple functions
# 4. Functions should only perform a single task
# If your function contains the keyword 'and' you can probably split it into two functions. Let's look at an example:

# This is bad
def fetch_and_display_personnel():
    data = # ...

    for person in data:
        print(person)


# This is good
def fetch_personnel():
    return # ...

def display_personnel(data):
    for person in data:
        print(person)
      
# Functions should do one thing and, as a reader, they do what you expect them to do.

# A good rule of thumb is that any given function shouldn't take longer than a few minutes to comprehend. Go back and review some of your old code that you wrote a few months ago. You should probably refactor any function that takes longer than five minutes for you to understand. This is your code after all. Think about how long it will take another developer to understand.

# 5. Keep your arguments at a minimum
# The arguments in your function should be kept to a minimum. Ideally, your functions should only have one to two arguments. If you need to provide more arguments to the function, you can create a config object which you pass to the function or split it into multiple functions.

# Example:

# This is bad
def render_blog_post(title, author, created_timestamp, updated_timestamp, content):
    # ...

render_blog_post("Clean code", "Nik Tomazic", 1622148362, 1622148362, "...")


# This is good
class BlogPost:
    def __init__(self, title, author, created_timestamp, updated_timestamp, content):
        self.title = title
        self.author = author
        self.created_timestamp = created_timestamp
        self.updated_timestamp = updated_timestamp
        self.content = content

blog_post1 = BlogPost("Clean code", "Nik Tomazic", 1622148362, 1622148362, "...")

def render_blog_post(blog_post):
    # ...

render_blog_post(blog_post1)

# 6. Don't use flags in functions
# Flags are variables (usually booleans) passed to functions, which the function uses to determine its behavior. They are considered bad design because functions should only perform one task. The easiest way to avoid flags is to split your function into smaller functions.

text = "This is a cool blog post."


# This is bad
def transform(text, uppercase):
    if uppercase:
        return text.upper()
    else:
        return text.lower()

uppercase_text = transform(text, True)
lowercase_text = transform(text, False)


# This is good
def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

uppercase_text = uppercase(text)
lowercase_text = lowercase(text)

# 7. Avoid side effects
# A function produces a side effect if it does anything other than take a value in and return another value or values. For example, a side effect could be writing to a file or modifying a global variable.
