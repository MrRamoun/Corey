# Functions

functions are some instructions packaged together to perform a specific task.

functions act as a black box with input/output terminals


## creating a function

```python
def func():
    pass # we want to keep this blank but we dont't want erros due to indentaion.
```

## functions call

```python
def func():
    pass
print(func()) # function calls are statements
```

## functions that return a value

functions that return a value are treated as variables of the same type as the returned value.

```python
def text():
    return "some text"

print(text().upper())
```

## functions with paramaters

```python
def fun(param): 
    # param is a local varabile to teh scope of the fun function and we don't have to worry about it affecting any other part of our code. THAT'S WHY SCOPES ARE AWESOME.
    return param

print(fun('hi')) 
```

## default value parameters

parameters with no default values are required arguments.

default values are used as a fall back if the arguments are not passed in.

> **Remember**: required positional (non-default) arguments have to come before (default) keyword arguments. creating functions with those out of order, will throw an error.

consider this scenario: what if the function got 2 args: one default and another one non-default. And only one argument was passed in. Where does that passed value belong to?.

```python
def hello(greeting='hello', name): 
    return '{} {}'.format(greeting, name)

# SyntaxError: non-default argument follows default argument
hello('ramoun', 'hi')
```

```python

def hello(name, greeting='hello'): # just to keep things intutive
    return '{} {}'.format(greeting, name)
```

> **Note**: the interpreter checks for SyntaxErrors first before executing the program.

> **Remember**: if a function takes only 2 required positional (non-default) arguments, and only one was given, that argument will be passed in to the first required positional argument only.

## order does matter

It's known that arguments have to be passed in order.

```python
def call(name, age, prof="student"):
    print(f'{name} is a modest {age} {prof}')

call(age=25, 'ramoun') # raises SyntaxError
call(age=25, name='ramoun')
```

## choosing the default arg we want

```python
def call(name,  age=23, prof="student"):
    print(f'{name} is a modest {age} {prof}')

call('ramoun', prof="engineer")    
# ramoun is a modest 23 engineer
```

## packing and unpacking args

### packing args:

- tuple packing

    in python you can compress all passed arguments into one argument of type `<class 'tuple'>`.
    
    ```python
    def func(*args):
        return args 

        print(func(1,2,3,4,'ramoun')) # output: (1, 2, 3, 4, 'ramoun')
        print(type(func(1,2,3))) # output: <class 'tuple'>
    ```
    
    ```python
    def func(*args):
        args[2] = 22
        return args[2]

    print(func(1,2,3,4,'ramoun'))
    print(type(func(1,2,3)))
    # ouptut:
        # TypeError: 'tuple' object does not support item assignment
    ```

- dictionary packing

    in python you can compress all passed keyword arguments into one argument of type `<class 'dict'>`.
    
    ```python
    def func(**kwargs):
        return kwargs 

    print(func(name='ramoun', age=22)) 
    # output: {'name': 'ramoun', 'age': 22}
    print(type(func()))
    # output: <class 'dict'>
    
    ```
    
    ```python
    def func(**kwargs):
        kwargs['name'] = 'hi'
        return kwargs

    print(func(name='ramoun'))
    # ouptut: {'name': 'hi'}
    ```
    
> **Remember**: packing is very useful in cases when we don't know how many positional (non-default) args passed in or how many keyword (default) args passed in.

> **Note**: `*args` and `**kwargs` are conventions. you can use any name you want. but it is always good to stick to the convention so other people can understand your code.

> **Important**: `*args` has to come before `**kwargs` or a SyntaxError will be thrown (in **declaration** and in **call**).

```python
def fun(*args, **kwargs):
    return (args, kwargs)

print(fun(age=22, 'hello', name='ramon'))    
```
>>SyntaxError: positional argument follows keyword argument

### unpacking args:

- tuple, list, set unpacking

    in python you can convert a (list,tuple,set,iterable,iterator ..etc) into multiple required positional args (unpack values) to pass them (individually) to a funciton respectivly.

    ```python
    def fun(name,age):
        return (name, age)

    t = ('ramoun', 22)
    l = ['michael', 33]
    s = {'jack', 15}

    print(fun(*t)) # ouput: ('ramoun', 22)
    print(fun(*l)) # ouput: ('michael', 33)
    print(fun(*s)) # ouput: ('jack', 15)
    ```


- dictionary unpacking

    in python you can convert a (dictionary) into multiple keyword args (unpack values) to pass them (indvidually) to a funciton respectivly.

    ```python
    def fun(name,age):
        return (name, age)

    d = {'name': 'ramoun', 'age': 22}

    print(fun(**d)) # ouput: ('ramoun', 22)
    ```

    > **Note**: if you used anything but dictionaries after the `**`, a TypeError would be raised.
    ```python
    TypeError: fun() argument after ** must be a mapping, not tuple
    ```

    ```python
    def fun(name='john', age=22):
        return (name, age)

    d = {'name': 'ramoun'}

    print(fun(**d)) # output: ('ramoun', 22)
    print(fun({})) # output: ({}, 22)
    print(fun()) # output: ('john', 22)
    ```



## final toughts about params and args

1. if all params are non-default params then they are **required positinal arg**. That means **Order** matters (in call) and the arg is **required** or it will raise an error. You can also use keywords in the call if you want.

2. if you add default params then you gotta follow the rules: 
    1. **required positional arguments** must always come first (in call & declaration). [intuitive] 
    1. order still matters for non-default args (**required positional argumetns**) (in call & declaration).
    1. order does also matter for default args (in call and declaration).
    1. you can override the order of default args by choosing what args to override using their kw-names (in call).
    1. and just like the required positional args, you can use keywords in the call.

1. for packing & unpacking in method: use `*` for required positional args & use `**` for default args:
    1. same rules of default and non-default args are applied here too.Because obviously they are the same just packed or unpacked.
    1. `*` -> tuple, `**` -> dict
