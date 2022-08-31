from functools import reduce

# Lambda
lambda_1 = lambda x: x * 10
lambda_2 = lambda x, y: x * y

print(lambda_1(5))
print(lambda_2(5, 6))

points_2d = [(1, 2), (2, -1), (3, 5), (10, 11)]

# sorted
points_2d_sorted = sorted(points_2d, key=lambda x: x[1])
print(list(points_2d))
print(list(points_2d_sorted))

list_1 = [1, 2, 3, 4, 5, 6]

# filter
filtered_list = filter(lambda element: element % 2 == 0, list_1)
print(list(filtered_list))

# List comprehension
filtered_list_2 = [x for x in list_1 if x % 2 == 0]
print(filtered_list_2)

# reduce - when you need to apply a function to an iterable and reduce it to a single cumulative value

reduced_value = reduce(lambda x, y: x * y, list_1)
print(reduced_value)

# map function

list_2 = [1, 2, 3, 4, 5]
mapped_list = map(lambda element: element * 2, list_2)
print(list(mapped_list))
