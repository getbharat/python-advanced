class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, msg, value):
        self.msg = msg
        self.value = value


def value_check(x):
    if x > 100:
        raise ValueTooHighError('value too high')
    if x < 10:
        raise ValueTooSmallError('value too small', x)


try:
    value_check(200)
except ValueTooHighError as e:
    print(e)

try:
    value_check(5)
except ValueTooSmallError as e:
    print(e.msg, e.value)


