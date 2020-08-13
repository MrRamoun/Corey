# Lists, Tuples, and Sets

## Lists

just as the name implies, it allows us to work with lists of values.

### creating a list:

```python
l = [1,3,2,3]
l = list((1,2,3,4))
l = []
l = list()
```

> **Note**: check out the best and fastest way to create a list in python on [stackoverflow](https://stackoverflow.com/questions/20816600/best-and-or-fastest-way-to-create-lists-in-python)

### indexing:

same as string [indexing/slicing](https://github.com/MrRamoun/Corey/blob/master/python_beginner/strings.md "strings lesson on github")

### adding items to the list:

- adding an item to the end of the list

    ```python
    l = ['hi', 1, 2]
    l.append(300)
    print(l) # output: ['hi', 1, 2, 300]
    ```

- adding an item to a specific index (pos) in the list

    ```python
    l = ['hello', 1, 2.3]
    l.insert(1, 'python')
    print(l) # output: ['hello', 'python', 1, 2.3]
    ```
- adding multiple items at once
    ```python
    l = ['hello', 1, 2.3]
    l2 = ['i','luv','programming']
    l.extend(l2)
    print(l) # output: ['hello', 1, 2.3, 'i', 'luv', 'programming']
    ```

    > **Tip**: try using `.insert(l2)` & .`append(l2)` and see what's gonna happen.

> **Note**: lists in python can contain other lists.

### removing items from a list:

- removing item by value

    ```python
    l = [1,2,3]
    l.remove(2)
    print(l) # output: [1, 3]
    ```

- removing last item of a list

    ```python
    l = [1,2,3]
    l.pop()
    print(l) # output: [1, 2]
    ```
    > **Note**: `pop()` returns the removed item.
    > **Note**: `pop()` is very useful for creating a stack/queue.

- removing items by index

    ```python
    l = [1,2,3]
    l.pop(1)
    print(l) #output: [1, 3]
    ```

### sorting a list:

- strings are sorted alphabetically (by default)

    ```python
    names = ['michael', 'john', 'josh', 'david']
    names.sort()
    print(names) # output: ['david', 'john', 'josh', 'michael']
    ```

- numbers are sorted in ascending order

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    numbers.sort()
    print(numbers) # output: [1, 2, 3, 11, 33, 55, 12231]
    ```

- if i want to sort in reverse order

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    numbers.sort(reverse=True)
    print(numbers) # output: [12231, 55, 33, 11, 3, 2, 1]

    names = ['michael', 'john', 'josh', 'david']
    names.sort(reverse=True)
    print(names) # output: ['michael', 'josh', 'john', 'david']
    ```

    > **Note**: i could use `numbers.sort().reverse()`. but it is considered good practice to use the `reverse` parameter of the `.sort()` method.

- sorting without altering the original list

    ```python
    names = ['michael', 'john', 'josh', 'david']
    numbers = [3, 33, 55, 11, 2, 12231, 1]

    sorted_names = sorted(names)
    sorted_numbers = sorted(numbers)

    print(names)
    print(sorted_names)
    ```

    > **Note**: `sorted()` returns a sorted copy of the passed list.

### useful list methods:

- reversing a list
    
    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    numbers.reverse()
    print(numbers) # output: [1, 12231, 2, 11, 55, 33, 3]
    ```    

- minimum value of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(min(numbers)) # output: 1
    ```    
- maximum value of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(max(numbers)) # output: 12231
    ```    
- sum of values of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(sum(numbers)) # output: 112336
    ```   

- index of a value of a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print(numbers.index(12231)) # output: 5
    ```   
    > **Tip**: try to find out the index of a value of a non-existing element.

- check if a value in a list

    ```python
    numbers = [3, 33, 55, 11, 2, 12231, 1]
    print('ramoun' in numbers) # output: False
    ```
   
> **Tip**: try to apply these methods to the `names` list and checkout the results you'll get.

### converting lists into strings & vice versa:

- conversion of lists into strings

    ```python
    l = ['a','b','c']
    str_l = ', '.join(l)
    print(str_l) # output: a, b, c   
    ```

- conversion of strings into lists

    ```python
    l = str_l.split(', ')
    print(l) # output: ['a', 'b', 'c']
    ```
### Copying lists

- using assignment statemnets [<u style="color:crimson">caution</u>]

    ```python
    l = [1,2,3]
    l2 = l
    print(l2) # [1, 2, 3]
    print(hex(id(l))) # 0x7f025f4dea80
    print(hex(id(l2))) # 0x7f025f4dea80
    # 2 pointers to the same object
    ```
    > **Note**: using the assignment statement leads to creating two refrences to the same address. So, The assignment just copies the reference to the list, not the actual list, so both `l` and `l2` refer to the same list after the assignment.

    <img alt="photo illustrating how using the assignment statement work" src="https://github.com/MrRamoun/Corey/blob/4269729a32eb4ed18a298b290f7e30fd9d1511dd/python_beginner/download.jpeg">

- using `.copy()` method [<u style="color:lime">recommended</u>]

    ```python
    l = [1,2,3]
    l2 = l.copy()
    print(l2) # [1, 2, 3]
    print(hex(id(l))) # 0x7f025f4dea80
    print(hex(id(l2))) # 0x7f025eceea00
    ```
    > **Note**: using the assignment statement leads to creating two refrences to the same address. So, altering one of the refrences will affect the value of the main list.

    > **Note**: `list_obj.copy()` (available since **Python 3.3**)

- using slicing technique

    ```python
    l = [1,2,3]
    l2 = l[:]
    print(l2) # [1, 2, 3]
    print(hex(id(l))) # 0x7f025f4dea80
    print(hex(id(l2))) # 0x7f0278680140
    ```
    > **Note**: Alex Martelli's opinion (at least back in 2007) about this is, that it is a **weird syntax** and it does not make sense to use it ever. ;) (In his opinion, the next one (`list()`) is more readable).
    

- using built-in `list()` function:

    ```python
    l = [1,2,3]
    l2 = list(l)
    print(l2) # [1, 2, 3]
    print(hex(id(l))) # 0x7f025f4dea80
    print(hex(id(l2))) # 0x7f025f4747c0
    ```

- using built-in `copy.copy()` function:

    ```python
    import copy
    l = [1,2,3]
    l2 = copy.copy(l)
    print(l2) # [1, 2, 3]
    print(hex(id(l))) # 0x7f025f4dea80
    print(hex(id(l2))) # 0x7f025f4747c0
    ```
    > **Note**: This is a little slower than `list()` because it has to find out the datatype of old_list first.

- If the list contains objects and you want to copy them as well, use generic `copy.deepcopy()`

    ```python
    import copy
    l = [1,2,3]
    l2 = copy.deepcopy(l)
    print(l2) # [1, 2, 3]
    print(hex(id(l))) # 0x7f025f4dea80
    print(hex(id(l2))) # 0x7f025f4747c0
    ```
    > **Note**: Obviously the slowest and most memory-needing method, but sometimes unavoidable.

- **FinaL Desicion:**

    ```python
    import timeit
    l = list(range(20))
    min(timeit.repeat(lambda: l[:]))
    # 0.38448613602668047
    min(timeit.repeat(lambda: list(l)))
    # 0.6309100328944623
    min(timeit.repeat(lambda: l.copy()))
    # 0.38122922903858125
    ```
    as we can see, `l.copy()` is even faster than slicing mehtod. For more about list copying. see [this_question on stackoverflow](https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy-it-to-prevent "different methods to copy a list in python").


> **Note**: In python lists are passed by refrence.

## Tuples

tuples are immutable objects in python

### creating a tuple:

```python
t = ()
t = (3,) # try t = (3) and see what 's gonna happen
```

> **Tip**: if you want something to modify, you can use a list, but if you want something that you can loop through and acces you can use a tuple.

## Sets 

are groups of values that are unorddred and also have no duplicates.

### creating a set:

```python
s = {}
print(type(s)) # output: <class 'dict'>
s = {1,2,3,4,5}
print(type(s)) # output: <class 'set'>
s = set([1,2,3,4,5])
print(type(s)) # output: <class 'set'>
s = set()
print(type(s)) # output: <class 'set'>
```

### accesssing a set:

```python
s = {1,2,3,4,5,6,6}
for i in s:
    print(i)
```

### uses of a set:

sets are mostly used to check if a value is part of a set, and also to remove duplicate values because `sets` through away duplicates.

unlike lists or ruples, sets don't really care about order.

> **Note**: `sets` do membership tests a lot more efficiently than `lists` and `tuples`. Because sets are more optimized for this.

```python
s = {1,3,3,4}
print(4 in s)
```

### operations on sets:

- intersection: things in common
    ```python
    s1 = {'math','english','science'}
    s2 = {'math','c.s','german'}
    print(s1.intersection(s2))
    ```

- differences: things in s1 and not in s2

    ```python
    s1 = {'math','english','science'}
    s2 = {'math','c.s','german'}
    print(s1.difference(s2))
    ```

- union: things in both sets without repetetion

    ```python
    s1 = {'math','english','science'}
    s2 = {'math','c.s','german'}
    print(s1.union(s2))
    ```

- **Final Thoughts**

    sets can definitly be useful in the mentioned use cases.