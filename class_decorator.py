class Hello:
    def __init__(self):
        pass

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print("Start")
            result = fn(*args, **kwargs)
            print("End")
            return result

        return wrapper


@Hello()
def print_hello(name):
    print(f"Hello {name}")


print_hello("Bharat")
