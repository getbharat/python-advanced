def fun(a, b, *, c, d):
    print(a, b, c, d)


# fun(1, 2, 4, 5), would not work as c and d should be keyword argument
fun(1, 2, c=4, d=5)
