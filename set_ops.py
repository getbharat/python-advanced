# Sets : unordered, no-duplicate, mutable
my_set = {1, 2, 3, 4, 5}
my_set_1 = set("Hello")
print(my_set)
print(my_set_1)

# Add number
my_set.add(6)
print(my_set)

# Clear set
my_set_2 = {1, 3, 4, 5}
print(my_set_2)
my_set_2.clear()
print(my_set_2)

# Length
print(len(my_set))

# Remove value
my_set_3 = {1, 3, 4, 5}
my_set_3.remove(3)
print(my_set_3)

# Removes arbitrary value, raise key error if element not found
my_set_4 = {1, 2, 3, 4, 5}
print(my_set_4.pop())
print(my_set_4)

# Use discard if not sure key is present
my_set_5 = {1, 2, 3, 4, 5}
my_set_5.discard(7)
print(my_set_5)

# Iterate set
for x in my_set_5:
    print(x)

# Check if element is present
if 5 in my_set_5:
    print("Yes")
else:
    print("No")

#  Intersection
set_a = {1, 2, 3, 4, 5, 6}
set_b = {5, 6, 7, 8, 9, 10}
print(set_a.intersection(set_b))

# Union
print((set_a.union(set_b)))

# Difference of two sets
print(set_a.difference(set_b))

# Symmetric difference, returns all element except that are common
print(set_a.symmetric_difference(set_b))

# Updating a set
set_c = {1, 2, 3, 4, 5, 6}
set_d = {5, 6, 7, 8, 9, 10}
set_c.update(set_d)
print(set_c)
