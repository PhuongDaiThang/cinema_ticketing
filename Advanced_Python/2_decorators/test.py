def my_decorator(func):
    def wrapper():
        print("Trước khi gọi hàm")
        func()
        print("Sau khi gọi hàm")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()