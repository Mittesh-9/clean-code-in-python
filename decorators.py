# In this section, we'll look at some Python concepts and tricks, which we can use to write better code.

# Decorators
# Decorators are an extremely powerful tool in Python, which allows us to add some custom functionality to a function. At its core, they are just functions called inside functions. By using them we take advantage of the SoC (Separation of concerns) principle and make our code more modular. Learn them and you'll be on your way to Pythonic code!

# Let's say we have a server, which is protected with a password. We could either ask for the password in every server method or create a decorator and protect our server methods like so:

def ask_for_passcode(func):
    def inner():
        print('What is the passcode?')
        passcode = input()

        if passcode != '1234':
            print('Wrong passcode.')
        else:
            print('Access granted.')
            func()

    return inner


@ask_for_passcode
def start():
    print("Server has been started.")


@ask_for_passcode
def end():
    print("Server has been stopped.")


start() # decorator will ask for password
end()   # decorator will ask for password
# Our server will now ask for a password every time start() or end() is called.
