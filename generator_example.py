def my_generator():
    yield 1
    yield 2
    yield 3


def my_generator_1():
    yield 1
    yield 2
    yield 3


g = my_generator()

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

# prints the next sum of next value
print(sum(g))

g1 = my_generator_1()

print(sum(g1))

