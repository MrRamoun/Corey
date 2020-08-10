"""
Combination:
    All the different ways which can be useed to group some values in which the order doesn't matter.
Permutations:
    All the different ways that can be used to group some values in which the order does matter.
"""

#%%
import itertools

my_list = [1,2,3]

combinations = itertools.combinations(my_list, 2)

for c in combinations:
    print(c)


# %%
import itertools

my_list = [1,2,3]

permutations = itertools.permutations(my_list, 3)

for p in permutations:
    print(p)    

# %%
# new cell