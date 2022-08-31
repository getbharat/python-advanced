from timeit import default_timer as timer
# Ordered, immutable, text representation
my_string = "Hello World"

# Print a character of a string
print(my_string[1])

# Remove spaces
my_string_1 = "   Hello World   "
print(my_string_1)
my_string_1 = my_string_1.strip()
print(my_string_1)

# Check if string or char is present
my_string_2 = "Hello World"
if "llo" in my_string_2:
    print("Yes")
else:
    print("No")

# Print all chars of a string
for ch in "Hello World":
    if ch != ' ':
        print(ch)

# Replace a word or char
my_string_3 = "Hello World"
my_string_3 = my_string_3.replace("World", "Universe")
print(my_string_3)

# Split a string
my_string_4 = "How are you doing"
my_list = my_string_4.split(" ")
print(my_list)

# Join  the strings
my_string_4 = ' '.join(my_list)
print(my_string_4)

# Slicing
my_string_5 = "Hello There!"
my_string_6 = my_string_5[::2]
print(my_string_6)

# Reverse string using slicing
my_string_7 = "Hello There!"
print(my_string_7[::-1])


my_string_8 = ["a"] * 1000000
# print(my_string_8)

# Bad code
concatenated_string = ''
start = timer()
for x in my_string_8:
    concatenated_string += x
end = timer()
print(end-start)
# print(concatenated_string)

# Good code
start_1 = timer()
my_string_9 = ''.join(my_string_8)
end_1 = timer()
print(end_1 - start_1)
# print(my_string_9)