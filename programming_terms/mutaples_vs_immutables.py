"""
Mutables: 
    are objects whose state cannot be modified (edited) after they are created.
Immutables:
    are objects whose state can be modified (edited) after they are created.
"""

# Immutables

## strings

string = "string"
print(string)
print("the memory address: ", str(id(string)) + " - " + str(hex(id(string))))

string = "another string" # it is not modifing an object -> it is creating a new object. (similar to: String string = "another string"; // in java)
print(string)
print("the memory address: ",  str(id(string)) + " - " + str(hex(id(string))))

# string[0] = "R"
# print(string) # 'str' object doesn't support item assignment -> that's because strings are immutable


# Mutables

## Lists

listy = [1,2,3]
print(listy)
print("addr of the list: ", hex(id(listy)))
print("addr of 0 element: ", hex(id(listy[0])))
print("addr of 1 element: ", hex(id(listy[1])))
print("addr of 2 element: ", hex(id(listy[2])))
print("- "*10)
listy[0] = 2147483670000008
print(listy)
print("addr of the list: ", hex(id(listy)))
print("addr of 0 element: ", hex(id(listy[0])))
print("addr of 1 element: ", hex(id(listy[1])))
print("addr of 2 element: ", hex(id(listy[2])))


## an example to demonstrate the idea behind the whole mutable/immutable thing.

employees = ['ramoun','jack','sami','brian']
output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print("address of output: ", hex(id(output))) # we are creating new object in each loop and that take up memory.

output += '</ul>\n'

print(output)


## summary

"""
1. We can check whether a data is mutable or not by printing out the id(memory address) of an object after performing an modification to the data type.

2. Lists are mutable in Python. We can change one item of the list while keeping the memory address of the entire list the same.

3.  Why should we know this concept? There are 2 reasons:
        a-  We can avoid and fix errors caused by modifying an immutable data type.
        b- We can speed up our programs. Memories are being shifted when performing operations on immutable objects means that it is going to take a lot more amount of time, and making our program slower. By avoiding operations on immutable data and thus the memory shift, we can improve our program speed.
"""

"""
Note:
    instead of appending to an output string at each step, we could have instead appended to a result list and then printed out that list after the iteration was complete. And if you only need a simple delimiter when displaying a list, you could use join, e.g. '-'.join(employees)
"""
