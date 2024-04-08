# Modularity and Classes
# In order to keep your code as organized as possible, you should split it into multiple files which are then split up into different directories. If you're writing code in an OOP-oriented language you should also follow basic OOP principles like encapsulation, abstraction, inheritance, and polymorphism.

# Splitting code into multiple classes will make your code easier to understand and maintain. There is no fixed rule on how long a file or a class should be, but try your best to keep them small (preferably under 200 lines).

# Django's default project structure is a good example of how your code should be structured:

awesomeproject/
├── main/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── templates

  # Django is an MTV (Model - Template - View) framework, which is similar to an MVC framework that we discussed earlier. This pattern divides program logic into three interconnected parts. You can see that each app is in a separate directory and each file serves one specific thing. If your project is split into multiple apps, you should make sure that the apps don't depend too much on each other.
