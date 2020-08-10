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
import itertools

my_list = [1,2,3,4,6,6]

combinations = itertools.combinations(my_list, 3)

permutations = itertools.permutations(my_list, 3)

print([c for c in combinations]) # be careful -> we got two 6s and they are treated as 2 different numbers

# to avoid repetation -> we can convert it to a set.
print([c for c in combinations])

print([result for result in combinations if sum(result) == 10])

# permutations & combinations are iterators in python so they raise the StopIteration exception.