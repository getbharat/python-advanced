def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs.get(key))


foo(1, 2, 3, 4, 5, a1=89, b1=90)