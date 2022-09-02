def function(*args, d):
    for arg in args:
        print(arg)
    print(d)


# function(1, 2, 3)  , Would not work

function(1, 2, 3, d=8)


