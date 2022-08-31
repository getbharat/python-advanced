def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


fib = fibonacci(5)

for x in fib:
    print(x)
