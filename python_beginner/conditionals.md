# conditionals

## if

    - Syntax
 
    condtion = True # evaluation
    if condition:
        # statement
    elif condition:
        # statement
    else:
        # statement

> **Note**: `conditoin` is any Boolean Expression that is valid an can be evaluated to either `True` or `False`.

```python
if True:
    print("this should be shown on the screen")

if False:
    print('this will never be shown on the screen')
```

### Comparisons:

    # Comparisons:
    # Equal:             ==
    # Not Equal:         !=
    # Greater Than:      >
    # Less Than:         <
    # Greater or Equal:  >=
    # Less or Equal:     <=
    # Object Identity:   is 'checking if values have the same address in memory'

```python
x = 60
if x > 20:
    print('> 20')
elif x > 30:
    print('> 30')    
elif x > 40:
    print('> 40')
elif x > 50:
    print('> 50')
elif x > 60:
    print('> 60')
elif x > 70:
    print('> 70')
elif x > 80:
    print('> 80')
else:
    print('sorry, stupid program.')
```

> **Note**: python doesn't have a switch-case statement because the `if`, `elif`, `else` statements are pretty clean enough to achieve the same goal.

### Bolean Operations:

    # and
    # or
    # not

```python
user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('welcome')
else: 
    print('please, log in.)
```

```python
user = 'admin'
logged_in = True

if not logged_in:    
    print('welcome')
else: 
    print('please, log in.)
```

### identity operator:

> **Note**: identity operator (`is`) tests if 2 objects have the same address which means they are both the same object in memory. Because 2 objects can acutally be equal and not be the same object in memory.

```python
a = [1,2,3]
b = [1,2,3]

print(a == b) # output: True  -> equal in value
print(a is b) # output: False -> are not the same object

print(id(a) == id(b)) # this is the same as (a is b)

# conclusion: 2 different objects with the same value.
```

## boolean VAlues evaluation in python

It is actually very easy -> the following values python considers them `False` and any thing else is `True`.

    # False Values:
        # False
        # None
        # Zero of any numeric type
        # Any empty sequence. For example, '', (), [].
        # Any empty mapping. For example, {}.

Let's test them out:

```python
condition = False
if condition:
    print('works')
```

```python
condition = None
if condition:
    print('works')
```

```python
condition = 0
if condition:
    print('works')
```

```python
condition = ''
if condition:
    print('works')
```

```python
condition = {}
if condition:
    print('works')
```

> **Tip**: Knowing this is very useful. let's say you have a function or something that suppose to return some values and you need to check if those values are actually there, you can pass in these sequences into a conditional to check wether a string is empty or a dictionary is empty and you don't have to call any specific method.

> **Note**: There is alos some user-defined class that can evaluate to `False`.