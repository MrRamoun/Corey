'''
"Therefore, in simple terms: A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing".

Clossures:
    a closure is a record storing a function together with an environment. The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created. Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

* A closure: closes over the free variables from their environment.    

* Closures are mostly used as templates.
'''
#%%
def outer():
    msg = 'hi'

    def inner():
        print('addr of inner: ', hex(id(inner)))

    # return inner() # calls inner() and returns None
    return inner # removing the parenthises -> returning function as an obj without execution (there is no call to the function) [i.e first-class function]

inner_from_outside = outer()
print('addr of inner_from_outside: ', hex(id(inner_from_outside)))
print('inner_from_outside: ', inner_from_outside)
inner_from_outside()


#%%
def outer():
    msg = 'hi'
    def inner():
        return msg

    return inner        

outer_from_outside = outer
inner_from_outside = outer_from_outside()

print(inner_from_outside())

#trying to see the difference between cosures and first-class functions
print()
print("outer_from_outside", (outer_from_outside))
print("inner_from_outside", (inner_from_outside))


#%%
def outer(arg_outer):
    def inner():
        return arg_outer

    return inner        

# trying to figure out how closures remmber vars.
# I believe that <locals> thing has something to do with closures remembering vars.
inner_from_outside = outer("ramoun")
print(inner_from_outside())
outer("kamel") 
# inner_from_outside = outer('hi')
print(inner_from_outside())

print(inner_from_outside)




#%%
def logger(msg):
    def log_msg():
        print("log: ", msg) # NOTE: msg ->is a free variable because it is not actually defined in the log_msg() but we still have access to it from within the log_msg()
    return log_msg

log_hi = logger('hi')
log_hi()



#%%
def html_tag(tag):
    def html_content(content):
        print("<{0}>{1}</{0}>".format(tag, content))
    return html_content

h1_tag = html_tag("h1")
print(h1_tag("hello")) # smart function that remembers local variables even outside of the scope => closure

"""
Long Storgy Short: 
    first class funcs: are functions treated as objects by ommiting the '()'
"""


#%%

def outer(arg1):
    def inner(arg2):
        return arg1 + ' ' + arg2
    return inner

inner_from_outside = outer('hi')
inner_from_outside('ramoun')
#%%

# first class fun (short lesson)
def x():
    pass

# f = x
# return x
# y(x)






# %%
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):

        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)



#%%
# x depends on y
# y1,y2,y3
# x1,x2,x3

# y1 -> x1
# y1 -> x2
# y1 -> x3
# y2 -> x1   # and so on...

# where y is outer function and x is inner function