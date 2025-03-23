def uppercase(func):

    def wrapper():
        return func().upper()

    return wrapper

@uppercase
def greet():
    return "привет!"

print(greet())