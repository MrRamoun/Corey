nums = [1,2,3,4,5,6,7,8,9]
result = []

# I want 'n' for each 'n' in nums

for n in nums:
    result.append(n)
print("using the traditonal for loop:")    
print(result)

result = [n for n in nums]
print("using comprehension for loop:")
print(result)


print('* ' * 40)
# I want 'n*n' for each 'n' in nums

result = []
for n in nums:
    result.append(n*n)
print("using the traditional loop:")
print(result)

result = [n*n for n in nums]
print("using the comprehension loop:")
print(result)


print('* ' * 40)
# using a map + lambda

result = map(lambda n: n*n, nums) # problem with readablity + high learning curve compared to comprehnsions
print("lambda + map")
print(result)


print('* ' * 40)
# I want 'n' for each 'n' in nums if n is even

result = []
for n in nums:
    if n % 2 == 0:
        result.append(n)
print(result)

result = [n for n in nums if n%2 == 0]
print(result)

print('* ' * 40)
# using lambda functions

result = filter(lambda n: n%2, nums) # same lambda problems compared to comprehensions
print(result)


print('* ' * 20)
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

result = []
for letter in 'abcd':
    for num in range(4):
        result.append((letter, num))
print(result)

result = [(letter,num) for letter in 'abcd' for num in range(4)]
print(result)


print('* ' * 20)
# Dictionaries
# zip creates a list of tuples that matches up one to one

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

superheros = zip(names,heros)

# I want a dict{'name':'hero'} for each (name,hero) pair in zip(names,heros)

result = {}
for superhero in superheros:
    result[superhero[0]] = superhero[1]
print(result)    

result = {}
for name,hero in zip(names,heros):
    result[name] = hero
print(result)    

result = {name: hero for name, hero in zip(names,heros)}
print(result)

# adding rules and restrictions to comprehensions
result = {name: hero for name, hero in zip(names, heros) if name != 'Clark'}
print(result)


print('* ' * 20)
# set comprehensions
# a set is like a list except it has all unique values
nums = [10,1,1,2,1,3,3,3,4,10,5,6,7,2,1,6,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)   
print(type(my_set))

my_set = set(nums)
print(my_set)
print(type(my_set))

my_set = {n for n in nums}
print(my_set)
print(type(my_set))


print('* ' * 20)
# generators
# I want to yield 'n*n' for each 'n' in nums

def gen_fun(nums):
    for n in nums:
        yield n*n

my_gen = gen_fun(nums)
print(my_gen)

for i in my_gen:
    print(i)

# generator's comprehension syntax is identical to list's but instead of brakcets -> parenthesis

my_gen = (n*n for n in nums)
print(my_gen)













