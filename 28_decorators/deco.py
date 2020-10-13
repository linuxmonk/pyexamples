def my_decorator(original_func):
    def wrapper():
        print("do something before")
        original_func()
        print("do something after")

    return wrapper


@my_decorator
def greeting():
    print("Hello World")


greeting()
