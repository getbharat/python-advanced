try:
    a = 5 / 0
    b = a + 5
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything worked fine")
finally:
    print('clean up')
