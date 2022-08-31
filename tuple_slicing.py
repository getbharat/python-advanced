my_tuple = 1, 2, 4, 5, 6, 7  # '()' are optional for tuple

print(my_tuple)

print(my_tuple[1:4])

# Reverse the tuple
print(my_tuple[::-1])

# Unpack a tuple
my_tuple_1 = "Bharat", 32, "Bangalore"

name, age, city = my_tuple_1
print(name)
print(age)
print(city)

# unpack using *

my_tuple_2 = 1, 2, 3, 4, 5, 6, 7

first, *middle, last = my_tuple_2

print(first)
print(*middle)
print(last)