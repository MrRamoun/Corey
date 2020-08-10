'''
First-class function:
    A PL is said to have a Frist-class function if it treats functions as first-class citizens.
    
First-class citizen (programming):
    fcc (sometimes called First-class objects) in PL is an entity which supports all the operations generally available to other entities. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.

* Long Story short: F-C func -> is a function that is treated as an obj that supports beign passed as an arg, returned from a func, and assigned to a var.
'''

def sq(n):
    return n*n

def cu(n):
    return n*n*n

value = sq(5) # using () == execution
square = sq

print(value)
print(square)
print(sq)
print(square(6))


# building our own map function
def my_map(function, array):
    result = []
    for item in array:
        result.append(function(item))
    return result

print('-'*20)
squares = my_map(square, [1,2,3,4,5,6,7,8,9]) # note: we are not adding parenthsis afterwards the 'square' because that will yield to executin' the functiont trying to get result as value to be placed instead of the function.

print(squares)

cubes = my_map(cu, [1,2,3,4,5,6,7])
print(cubes)

