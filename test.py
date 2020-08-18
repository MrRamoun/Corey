import random

def hello():
    random_var = random.randint(1, 10)
    return random_var

print = hello

print()

input = 'hi'

# input() # str obj is not callable -> 'hi'()

# 'hi'()
