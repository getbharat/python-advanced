my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get sub list, index after colon is excluded
my_list_sliced = my_list[1:5]

print(my_list_sliced)

my_list_sliced2 = my_list[:5]

# If no index is mentioned before colon, it starts from 0
print(my_list_sliced2)

# step index
my_list_sliced3 = my_list[::2]  # every second element is picked
print(my_list_sliced3)

# A good way to sort, '-' represent last and 1 represent every first element. So ever first element from last.
my_list_sliced4 = my_list[::-1]
print(my_list_sliced4)

# Create a list of squares for a given list in one line
elements = [1, 2, 3, 4, 5]
square_list = [i * i for i in elements]
print(square_list)

#  Find Odd and event numbers
even_numbers = [i % 2 == 0 for i in elements]

print(even_numbers)

# copy
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [5, 6, 7, 8, 9]
my_list_2 = my_list_1
print(my_list_2)
