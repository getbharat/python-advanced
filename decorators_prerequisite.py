def outer_function():
    task = "Bharat"

    def inner_function():
        print("Hello " + task)

    return inner_function


my_function = outer_function()

my_function()

