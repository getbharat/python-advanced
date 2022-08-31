# Difference update
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3, 4, 8, 10, 11}

set_a.difference_update(set_b)

print(set_a)

# Subset and super set
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 8, 10, 11}

print(set_c.issubset(set_d))
print(set_d.issuperset(set_c))

# Symmetric difference
set_e = {1, 2, 3, 4, 5, 8}
set_f = {1, 2, 3, 4, 8, 10, 11}
set_e.symmetric_difference_update(set_f)
print(set_e)

# Disjoint, true if no common elements are found else false

set_g = {1, 2, 3, 4}
set_h = {1, 2, 3, 4, 8}
set_j = {9, 10}
print(set_g.isdisjoint(set_h))
print(set_g.isdisjoint(set_j))

# Copy

set_k = {1, 2, 3, 4}
set_l = set_k
set_l.add(5)
print(set_k)
print(set_l)

# Actual copy
set_m = {1, 2, 3, 4}
set_n = set_m.copy()
# set_n = set(set_m)
set_n.add(5)
print(set_m)
print(set_n)
