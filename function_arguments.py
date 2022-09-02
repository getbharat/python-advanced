"""
- Difference between argument and parameter
- Positional and keyword argument.
- Default argument
- Variable length argument ( *args and **kwargs)
- Container unpacking into function arguments
- Local vs. Global arguments
- Parameter passing ( by value or reference)

"""


def print_nums(a, b, c, d):
    print(a, b, c, d)


print_nums(1, 2, 3, 4)
print_nums(a=5, c=8, d=9, b=0)


def print_nums_default(a, b, c, d=5):  # parameters
    print(a, b, c, d)


print_nums_default(1, 2, 4, 6)  # arguments
print_nums_default(1, 2, 4)
