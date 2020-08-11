# %%

# strings work different than nums (remember)
# nums are created and then all have the same id but strings have different ids even if their values are the same.
# == -> for comapring values
# is -> for comapring ids
# in java -> use isequal() 

a = 'ab-c' #3
b = 'ab-c' #3
print('a is b : ' + str(a is b)) # False
print('a == b : ' + str(a == b))

print(hex(id(a)))
print(hex(id(b)))

print()
print(a[0] is b[0]) #True
print(a[1] is b[1]) #True
print(a[2] is b[2]) #True
print(a[3] is b[3]) #True

print()
print(hex(id(a[0])))
print(hex(id(b[0])))

# this is has to do with the language itself

# %%

# >>> a='abc';b='xyz'
# >>> a is 'abc'
# True
# >>> b is 'xyz'
# True
# >>> 'abc'+'xyz' is 'abcxyz'
# True
# >>> a+b is'abcxyz'
# False
# >>> c = 'abcxyz'
# >>> c is a+b
# False
# >>> c is 'abcxyz'
# True

# >>> a=257
# >>> b=257
# >>> a is b
# False
# >>> 257 is  257
# True

# >>> a=256
# >>> b=1
# >>> a+b is 257
# False
# >>> 256+1 is  257
# True
# >>> c=257
# >>> c is 257
# False
# >>> a+b is c
# False
# >>>



