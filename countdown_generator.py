# How generator executes

def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

print(next(cd))

