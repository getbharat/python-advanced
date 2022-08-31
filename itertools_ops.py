from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, \
    cycle, repeat
import operator

# Cartesian product
a = [1, 2]
b = [3]
prod = product(a, b)
print(list(prod))

#
prod_1 = product(a, b, repeat=2)
print(list(prod_1))

# Permutations
a1 = [1, 2, 3]
perm = permutations(a1, 2)
print(list(perm))

# Combinations, all possible combinations for given length
a2 = [1, 2, 3, 4]
comb = combinations(a2, 2)
print(list(comb))

# Combination  - all possible combinations including a number itself
comb_with_replacement = combinations_with_replacement(a2, 2)
print(list(comb_with_replacement))

# Accumulate
acc = accumulate(a2)
print(list(acc))

# Accumulate, use function a second argument

acc_mul = accumulate(a2, func=operator.mul)
print(list(acc_mul))

a3 = [1, 2, 3, 5, 4]
acc_max = accumulate(a3, func=max)
print(list(acc_max))

# Group by functions

person_list = [{'name': 'Bharat', 'age': 32, 'status': 'Active'}, {'name': 'Shawn', 'age': 32, 'status': 'InActive'},
               {'name': 'Ruby', 'age': 25, 'status': 'Active'}]

key = lambda element: element['status']
groupby_result = groupby(sorted(person_list, key=key), key)

for key, value in groupby_result:
    print(key, list(value))

# count

for i in count(10):  # infinite loop
    print(i)
    if i == 15:
        break

# Ranage

for i in range(0, 10):
    print(i)

# Cycle

list1 = [1, 2, 3, 4, 5]
for i in cycle(list1):  # Infinite loop, prints all numbers of list and then cycles again the list
    print(i)
    break

# Repeat
for i in repeat(2, 3):  # Infinite loop, can be restricted if number of times is given
    print(i)
