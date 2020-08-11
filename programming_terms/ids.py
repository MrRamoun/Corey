# %%
a = 'ab-c'
b = 'ab-c'
print(a is b) # False
print(a == b)
print(hex(id(a)))
print(hex(id(b)))
# a[0] is b[0], a[1] is b[1], a[2] is b[2],  a[3] is b[3] #(True, True, True, True)




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



