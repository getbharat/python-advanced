import sys
import timeit

my_tuple = 1, 2, 3, 4
my_list = [1, 2, 3, 4]

# Tuple is efficient if working with large data
print(sys.getsizeof(my_tuple), " bytes")
print(sys.getsizeof(my_list), " bytes")

print(timeit.timeit(stmt="[1,2,3,4,5,6]", number=10000))
print(timeit.timeit(stmt="1,2,3,4,5,6", number=10000))
