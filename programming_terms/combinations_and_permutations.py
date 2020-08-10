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


# %%
word = 'sample'
my_letters = 'ampsle'

c = itertools.combinations(my_letters, len(word))
p = itertools.permutations(my_letters, len(my_letters))

# to see why the following code won't find a match run a for loop to see all the elements of 'c'
for i in c:
    # combinations are not useful in this kind of problems
    if ''.join(i) == word:
        print("A match was found!")
        print(i)
else :
    print("no match found")

counter = 0
for i in p:
    counter += 1
    if ''.join(i) == word:
        print("A match was found!")
        print(i)
        break # it is important to stop when a match is found 
else: # it works only if now match was found but remember to include the 'break' in the boddy of the loop in order or the 'else' to work.
    print("no match found!")
    print(counter)