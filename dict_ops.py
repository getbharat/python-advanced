# Key value pair, unordered, mutable
my_dict = {"name": "Bharat", "age": 32, "city": "Bangalore"}

my_dict_1 = dict(name="Rhea", age=32, city="Bangalore")

print(my_dict)
print(my_dict_1)

my_dict["name"] = "Roy"

print(my_dict)

# Delete a key
del my_dict["name"]

print(my_dict)

my_dict.pop("age")

print(my_dict)

# Removes the last inserted (k,v)
my_dict_1.popitem()
print(my_dict_1)

# check if key is present
if "name" in my_dict_1:
    print(my_dict_1.get("name"))

# iterate a dict
for key in my_dict_1.keys():
    print(key)

for value in my_dict_1.values():
    print(value)

# iterate a dict, key and value in a same loop
for key, value in my_dict_1.items():
    print(key, value)

# Copy
my_dict_2 = {"name": "Bharat", "age": 32, "city": "Bangalore"}
my_dict_2_copy = my_dict_2
my_dict_2_copy["email"] = "abc@in.com"

print(my_dict_2)
print(my_dict_2_copy)

# Make actual copy
my_dict_3 = {"name": "Bharat", "age": 32, "city": "Bangalore"}
my_dict_3_copy = my_dict_3.copy()
my_dict_3_copy["email"] = "abc@in.com"
print(my_dict_3)
print(my_dict_3_copy)

# copy using dict function
my_dict_4 = {"name": "Bharat", "age": 32, "city": "Bangalore"}
my_dict_4_copy = dict(my_dict_4)
my_dict_4_copy["email"] = "abc@gmail.com"
print(my_dict_4)
print(my_dict_4_copy)

# Merge dictionaries
my_dict_5 = {"name": "Aman", "age": 50, "email": "abc@gmail.com"}
my_dict_5.update(my_dict_4)
print(my_dict_5)

# Use tuple as key, but you can use list as a key
my_tuple = (1, 2)
my_dict_6 = {my_tuple: 3}
print(my_dict_6.get(my_tuple))

my_dict_7 = {3: my_tuple}
print(my_dict_7.get(3))

my_dict_8 = {3: [1, 2]}
print(my_dict_8.get(3))
