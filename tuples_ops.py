# Ordered, immutable, allows duplicate
my_tuple = ("Apple", 28, "banana")

print(my_tuple)

print(my_tuple[0])

# Create tuple using tuple function way
my_tuple_1 = tuple(["A", "B", "c", "A"])
print(type(my_tuple_1))
print(my_tuple_1[0])

for item in my_tuple_1:
    print(item)

# Check if element is present
if "A" in my_tuple_1:
    print("Yes")
else:
    print("No")

# Length
print(len(my_tuple_1))

# Count of an element
print(my_tuple_1.count("A"))
print(my_tuple_1.count("o"))

# Print index of a element
print(my_tuple_1.index("A"))
print(my_tuple_1.index("J"))  # Throws error
