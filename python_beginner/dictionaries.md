# Dictionary

dictionaries allow us to create key-value pairs. These are 2 linked values where the `key` is a unique identifier used to access our data and the value is our data

> **Note**: other languages call theses hash-maps..etc.

## Creating a Dictionary

```python
d = dict()
d = {}
```

```python
user = {
    'name': 'ramoun',
    'age': 24,
    'married': True,
    'hobbies': ['computers', 'computers', 'computers', 'science']
}
print(user['hobbies'])
```
> **Note**: `keys` can be of any immutable data type.

> **Tip**: when accessing a `key` that doesn't exist using the slicing mehtod, a **KeyError** will be raised. Instead use the `.get()` method.

```python
user = {
    'name': 'ramoun',
    'age': 24,
    'married': True,
    'hobbies': ['computers', 'computers', 'computers', 'science']
}
print(user.get("age"))
print(user.get('birth-date')) # output: None
# you can also specify a default value for keys that don't exisit.
print(user.get('phone', 'Not Found')) # output: 'Not Found'
```

## Adding a New Entry to a Dictionary

```python
user = {
    'name': 'ramoun',
    'age': 24,
    'married': True,
    'hobbies': ['computers', 'computers', 'computers', 'science']
}
# let's add a phone number
user['phone'] = '+201554112661'
print(user)
```


## Updating a value of a Dictionary

- using the slicing method

    ```python
    user = {
        'name': 'ramoun',
        'age': 24,
        'married': True,
        'hobbies': ['computers', 'computers', 'computers', 'science']
    }
    # let's add a phone number
    user['age'] = 16
    print(user)
    ```

- using the `.update()` method

    ```python
    user = {
        'name': 'ramoun',
        'age': 24,
        'married': True,
        'hobbies': ['computers', 'computers', 'computers', 'science']
    }
    # let's add a phone number
    user.update({'age': 15, 'phone': '+201554112661'})
    print(user)
    ```
    > **Note**: the `.update()` is used to _update_ and _add_ mulitple entries to the dictionary.

## Removing an Entry

- using the `del` keyword

    ```python
        user = {
        'name': 'ramoun',
        'age': 24,
        'married': True,
        'hobbies': ['computers', 'computers', 'computers', 'science']
    }
    del user['age']    
    print(user)
    ```

- using the `.pop()` method 

    The pop method allows us to remove and return the removed.

    ```python
        user = {
        'name': 'ramoun',
        'age': 24,
        'married': True,
        'hobbies': ['computers', 'computers', 'computers', 'science']
    }
    age = user.pop('age')
    print(user)
    print(age)
    ```

## Counting How Many Entries

```python
len(dict({'age': 24, 'name': 'mark'}))
```

## Access Entries of a Dictionary

- Acessing keys
    
    ```python
    print(user.keys())
    ```

- Acessing values
    
    ```python
    print(user.values())
    ```

- Acessing keys & valuse
    
    ```python
    print(user.items())
    ```

- Looping through items

    > **Note**: looping through items like lists, tuples, and sets won't yield the same result in dictionaries.

    ```python
    d = {'name': 'linus', 'age': 30}
    for k in d:
        print(k)
    # output: name age
    # Note: only the keys were printed on the screen.
    ```
    
    The best way to do it is using the `.items()` 
    
    ```python
    d = {'name': 'linus', 'age': 30}
    for k,v in d.items(): # because d.items() return a pair of 2 value.
        print(k, v)
    ```

> **Note**: dictionaries are not ordered (why need order when you have the key).
> **Note**: order only matters when the actual keys and values are being created but not in the retrieving process.

```python
d = {'name': 'ramoun', 'name', 'hi'}
d['name'] # returns 'hi'
```
 
 
