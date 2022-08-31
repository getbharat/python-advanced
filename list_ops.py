my_list = ["apple", "banana", "cherry"]

print(my_list)

# Create empty list
my_list2 = list()
print(my_list2)

# Add element in a empty list
my_list2.append("apple")
my_list2.append(5)
my_list2.append(True)
print(my_list2[0])

# Get the last element
print(my_list2[-1])

# Iterate a list
for item in my_list2:
    print(item)

# check if element is present
if "apple" in my_list2:
    print("Yes")
else:
    print("No")

if "lemon" in my_list2:
    print("Yes")
else:
    print("No")

# length of list
print(len(my_list2))

# insert at specific index, other elements would be shifted accordingly
my_list2.insert(0, "mango")
print(my_list2)

# remove last element
my_list2.pop()
print(my_list2)

# remove specific element, make sure element is present otherwise exception is thrown
my_list2.remove("mango")

print(my_list2)

# Reverse the list
my_list2.reverse()

print(my_list2)

my_list3 = [5, 1, -2, 0, 3]

# sort the original list
my_list3.sort()

print(my_list3)

# If you don't want to change original list

my_list4 = [5, 1, -2, 0, 3]
my_list_sorted = sorted(my_list4)

print(my_list_sorted)
print(my_list4)

# Create a list with same elements
my_list5 = [1] * 5

print(my_list5)

# Concatenate list
list_concatenated = my_list5 + my_list4
print(list_concatenated)

# copy a list
my_list6 = ["a", "b", "c"]
my_list6_copy = my_list6

print(my_list6_copy)
my_list6_copy.append("d")

print(my_list6)
print(my_list6)

# Copy without using copy method

my_list7 = ["a", "b", "c"]
my_list7_copy = my_list7.copy()
my_list7_copy.append("d")
print(my_list7_copy)
print(my_list7)

# Copy using list function and slicing
my_list8 = ["a", "b", "c"]
my_list8_copy = list(my_list8)
my_list8_copy2 = my_list8[:]
my_list8_copy2.append("d")
print(my_list8)
print(my_list8_copy)
print(my_list8_copy2)
