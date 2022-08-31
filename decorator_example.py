def decorator_function(func):
    def print_func():
        print("Start")
        func()
        print("End")

    return print_func


# print_name = decorator_function(print_name)


# Will give the same output as above or print_name = decorator_function(print_name)
@decorator_function
def print_name():
    print("Bharat")


print_name()
