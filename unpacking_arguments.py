def foo(a, b, c):
    print(a, b, c)


li = (1, 3, 4)
li1 = [6, 7, 8]
foo(*li)
foo(*li1)

my_dict = {'a': 9, 'b': 10, 'c': 11}

foo(**my_dict)
