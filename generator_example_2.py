import sys


def sum_n_nums(n):
    num = 0
    sum_value = 0
    while num <= n:
        sum_value = sum_value + num
        num += 1
    return sum_value


result = sum_n_nums(10)

print(result)


# But if we use generator

def generator_sum(n):
    num = 0
    while num <= n:
        yield num
        num += 1


result = generator_sum(10)

print(sum(result))

print(sys.getsizeof(sum_n_nums(10000)))
print(sys.getsizeof(generator_sum(10000)))
