# String formatting using %, format and f"String"
gram = 1000
my_string = "1 kg has %d gram" % gram

print(my_string)

country = "India"

my_string_1 = "I love my %s " % country
print(my_string_1)

# using format

my_string_2 = "I love my {}".format(country)
print(my_string_2)

# Using f"String"

kg = 10
gram = 1000
my_string_3 = f"{kg} has {kg*gram} grams"

print(my_string_3)