"""
String Interpolation:
    The process of evaluating a string literal containing one or more {placeholders}, yielding the result in which the placeholders are replaced with their corresponding values.

methods of String Interpolatin in python:
    1. .format method with the help of '{}'.
    2. formatting text using (%) : we got this from c-lang.

!!NOTE: String 'Concatenation' is not String Interpolation.    
"""

#%%
# an example that shows the benifits of using interpolation over concatenation

name = 'RAMOUN'
age = 25

greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old.' # NOTE: implicit conversion of int to str is not allowed in python. You need to cast your int/float vars like i did here.

print(greeting)

# Problems with concatenation
    # 1. casting is needed (depending on the language).
    # 2. spacing should be considered in the strings themselves.
    # 3. 


# %%
# this is the equivelent string interpolation method.

name = 'RAMOUN'
age = 25

greeting_auto = 'My name is {} and I am {} years old.'.format(name, age) # replaced by order + can't add more than two '{}' or it will rais out of range IndexError

greeting_manual = 'My name is {0} and I am {1} years old. Remember {0} and {1} years old.'.format(name, age) # if indexes are used then the order doesn't matter + you can add as many of '{i}' as you like as long as you add the index or it won't work

# NOTE: if you mix '{}' with '{i}' it won't work and it will raise a ValueError exception: cannot switch from automatic field numbering to manual field specification

greetings_tidious = 'My name is {name} and {name} is cool {times}x times.'.format(name=name, times=age)

print(greeting_auto)
print(greeting_manual)
print(greetings_tidious)

# benifits of interpolation over concatenation:
#   1. easier to read
#   2. less prone to errors (no casting / spacing and stuff - because in concatensation you may mess a space somewhere)
#   3. it is pretty much like a template
#   4. can be used as html template to add values from a database.


# %%
# for python 3.6+ there is f-strings

f_string = f'i am {age} and my name is {name}'

print(f_string)
